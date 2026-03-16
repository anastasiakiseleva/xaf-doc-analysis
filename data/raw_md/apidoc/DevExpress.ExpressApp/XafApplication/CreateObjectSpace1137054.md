---
uid: DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)
name: CreateObjectSpace(Type)
type: Method
summary: Creates an [Object Space](xref:113707) that supports a specific object type. Use this method overload if your application registers several [ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider)s.
syntax:
  content: public IObjectSpace CreateObjectSpace(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A System.Type object that is the type of objects that will be supported by a created Object Space.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the created Object Space.
seealso: []
---
Use the **CreateObjectSpace** method to create an [Object Space](xref:113707) in your application. You may require a new Object Space if, for example, you need to create a [View](xref:112611).

The **CreateObjectSpace(System.Type)** method initially calls the [XafApplication.CheckCompatibility](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibility) method to check whether the versions of the application and its modules coincide with the corresponding versions in the database. Then, a new Object Space is created if the versions coincide. For instance, when a developer modifies the database while end-users are using this database, an exception is raised when an end-user tries to invoke a View. This exception will report that the database version is greater than the application's version. You can override this behavior by handling the [XafApplication.CustomCheckCompatibility](xref:DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility) event.

To create an Object Space, the [XafApplication.ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider)'s [IObjectSpaceProvider.CreateObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceProvider.CreateObjectSpace) method is used. The type of the Object Space that will be created by this method depends on the type of the Object Space Provider:

Space Provider | Object Space
---------|----------
@DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider | @DevExpress.ExpressApp.Xpo.XPObjectSpace
@DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 | @DevExpress.ExpressApp.EFCore.EFCoreObjectSpace
@DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider | @DevExpress.ExpressApp.Security.SecuredXPObjectSpace
@DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 | @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace
@DevExpress.ExpressApp.NonPersistentObjectSpaceProvider | @DevExpress.ExpressApp.NonPersistentObjectSpace

> [!NOTE]
> [!include[Object Space Providers Order](~/templates/objectspaceprovidersorder.md)]

When several Object Space Providers are passed to the [XafApplication.ObjectSpaceProviders](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProviders) property, pass the _objectType_ parameter to the **CreateObjectSpace** method to create an Object Space that supports a particular object type.

You can access the created Object Space by handling the [XafApplication.ObjectSpaceCreated](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated) event.

To create a nested Object Space, use the [XPObjectSpace.CreateNestedObjectSpace](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace) method.

The following example creates a [List View](xref:112611#list-view) and displays it via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class ShowListViewController : WindowController {
    public ShowListViewController() {
        PopupWindowShowAction showListViewAction = new PopupWindowShowAction(this, "ShowListView",
            PredefinedCategory.Edit);
        showListViewAction.CustomizePopupWindowParams += ShowListViewAction_CustomizePopupWindowParams;
    }
    private void ShowListViewAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        Type objectType = typeof(Person);
        IObjectSpace newObjectSpace = Application.CreateObjectSpace(objectType);
        e.View = Application.CreateListView(newObjectSpace, objectType, true);
    }
}
```
***