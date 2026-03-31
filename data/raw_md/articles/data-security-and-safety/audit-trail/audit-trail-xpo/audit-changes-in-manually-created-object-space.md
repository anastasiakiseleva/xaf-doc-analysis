---
uid: "403869"
title: 'Audit Changes in a Manually Created ObjectSpace'
---
# Audit Changes in a Manually Created ObjectSpace

The Object Space API helps you manage data stores in XAF applications. To access the API, you usually need to call the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)) method that initializes an `XPObjectSpace` object. The **Audit Trail Module** then automatically tracks all changes in the new object space.

If you create an `XPObjectSpace` manually (for example, a non-secured object space in a secured application), the **Audit Trail Module** does not log changes made within this `XPObjectSpace`. To enable audit, register the object space and handle its events as shown below:

# [C#](#tab/tabid-csharp-net6)
 
```csharp{30,33-35,41-48}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Security.ClientServer;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Persistent.Base;
using MySolution.Module.BusinessObjects;
using System;
using System.Linq;
// ...
public class CustomWinController : ObjectViewController<DetailView,Contact> {
    IAuditTrailService auditTrailService;

    [ActivatorUtilitiesConstructor]
    public CustomController(IAuditTrailService auditTrailService) : this() {
        this.auditTrailService = auditTrailService;
    }

    public CustomWinController() {
        var myAction1 = new SimpleAction(this, "MyWinAction1", PredefinedCategory.Edit);
        myAction1.Execute += MyAction1_Execute;
    }

    private void MyAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
        SecuredObjectSpaceProvider securedObjectSpaceProvider = (SecuredObjectSpaceProvider)
            Application.ObjectSpaceProviders.First(
                p => p is SecuredObjectSpaceProvider
            );
        // Create a 'free' XPObjectSpace
        IObjectSpace unsecuredObjectSpace = securedObjectSpaceProvider.CreateNonsecuredObjectSpace(); 
        var _contact = (Contact)unsecuredObjectSpace.GetObject(View.CurrentObject);

        auditTrailService.BeginSessionAudit(((XPObjectSpace)unsecuredObjectSpace).Session, AuditTrailStrategy.OnObjectChanged);
        unsecuredObjectSpace.Committed += new EventHandler(ObjectSpace_Committed);
        unsecuredObjectSpace.Reloaded += new EventHandler(ObjectSpace_Reloaded);

        _contact.LastName = "NewName" + DateTime.Now.Millisecond;
        unsecuredObjectSpace.CommitChanges();
    }

    private void ObjectSpace_Reloaded(object sender, EventArgs e) {
        auditTrailService.EndSessionAudit(((XPObjectSpace)sender).Session);
        auditTrailService.BeginSessionAudit(((XPObjectSpace)sender).Session, AuditTrailStrategy.OnObjectChanged);
    }
    private void ObjectSpace_Committed(object sender, EventArgs e) {
        auditTrailService.SaveAuditData(((XPObjectSpace)sender).Session);
        auditTrailService.BeginSessionAudit(((XPObjectSpace)sender).Session, AuditTrailStrategy.OnObjectChanged);
    }

}
```
***

[`CreateNonsecuredObjectSpace`]: DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.CreateNonsecuredObjectSpace
