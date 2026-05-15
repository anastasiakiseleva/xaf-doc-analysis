---
uid: "112916"
seealso:
- linkId: "113684"
- linkId: "402158"
- linkId: "112617"
- linkId: "402985"
title: 'How to: Store Application-Wide Settings Using a Singleton Business Object'
---
# How to: Store Application-Wide Settings Using a Singleton Business Object

A singleton is a business class that has only one instance that cannot be deleted. Singletons are useful for storing application-wide settings, company information, or other unique configuration data. This scenario creates a singleton class and displays its Detail View in your application.

If you implement this solution in a multi-tenant application, singleton data is persisted in each tenant database (tenant-specific settings). If you need global settings shared by all tenants, use the following technique instead: [Shared Data Support in a Multi-Tenant Application](xref:405451).

> [!Tip]
> A complete sample project is available in the following GitHub Example: [XAF - How to implement a singleton class](https://github.com/DevExpress-Examples/xaf-how-to-implement-a-singleton-class).

## Implement a Singleton

1. To prohibit singleton deletion and creation of additional singletons, use the [Validation Module](xref:113684). Apply the following attributes: [RuleObjectExists](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute) and [RuleCriteria](xref:DevExpress.Persistent.Validation.RuleCriteriaAttribute):

    **File:** _SingletonSolution.Module\BusinessObjects\Singleton.cs_

    # [EF Core](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.Persistent.Validation;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;

    namespace SingletonSolution.Module.BusinessObjects {
        [RuleObjectExists("AnotherSingletonExists", DefaultContexts.Save, "True", InvertResult = true,
        CustomMessageTemplate = "Another Singleton already exists.")]
        [RuleCriteria("CannotDeleteSingleton", DefaultContexts.Delete, "False",
        CustomMessageTemplate = "Cannot delete Singleton.")]
        public class Singleton : BaseObject {
            public virtual string Name { get; set; }
            public virtual string Description { get; set; }
        }
    }
    ```

    # [XPO](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Persistent.Validation;
    using DevExpress.Xpo;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;

    namespace SingletonSolution.Module.BusinessObjects {
        [RuleObjectExists("AnotherSingletonExists", DefaultContexts.Save, "True", InvertResult = true,
        CustomMessageTemplate = "Another Singleton already exists.")]
        [RuleCriteria("CannotDeleteSingleton", DefaultContexts.Delete, "False",
        CustomMessageTemplate = "Cannot delete Singleton.")]
        public class Singleton : BaseObject {
            public Singleton(Session session) : base(session) { }
            private string name;
            public string Name {
                get { return name; }
                set {
                    SetPropertyValue("Name", ref name, value);
                }
            }
            private string description;
            public string Description {
                get { return description; }
                set {
                    SetPropertyValue("Description", ref description, value);
                }
            }
        }
    }
    ```

    # [VB.NET](#tab/tabid-vb-xpo)

    ```vb
    Imports DevExpress.Persistent.BaseImpl
    Imports DevExpress.Persistent.Validation
    ' ...
    <RuleObjectExists("AnotherSingletonExists", DefaultContexts.Save, "True", InvertResult := True, _
    CustomMessageTemplate := "Another Singleton already exists."), _
    RuleCriteria("CannotDeleteSingleton", DefaultContexts.Delete, "False", _
    CustomMessageTemplate := "Cannot delete Singleton.")> _
    Public Class Singleton
        Inherits BaseObject
        Public Sub New(ByVal session As Session)
            MyBase.New(session)
        End Sub
        Private _name As String
        Public Property Name() As String
            Get
                Return _name
            End Get
            Set(ByVal value As String)
                SetPropertyValue("Name", _name, value)
            End Set
        End Property
        Private _description As String
        Public Property Description() As String
            Get
                Return _description
            End Get
            Set(ByVal value As String)
                SetPropertyValue("Description", _description, value)
            End Set
        End Property
    End Class
    ```

    ***

2. If you use Entity Framework Core, add the `Singleton` type to your `DbContext`:

    **File:** _SingletonSolution.Module\BusinessObjects\SingletonSolutionDbContext.cs_

    # [EF Core](#tab/tabid-sharp-efcore1)
    ```csharp
    using DevExpress.ExpressApp.EFCore.Updating;
    using Microsoft.EntityFrameworkCore;
    using Microsoft.EntityFrameworkCore.Design;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.ExpressApp.Design;
    using DevExpress.ExpressApp.EFCore.DesignTime;
    using SingletonSolution.Module.BusinessObjects;

    namespace SingletonSolution.Module.BusinessObjects;

    //...
    public class SingletonSolutionDbContext : DbContext {
        public SingletonSolutionDbContext(DbContextOptions<SingletonSolutionDbContext> options) : base(options) {
        }
        //public DbSet<ModuleInfo> ModulesInfo { get; set; }
        //...
        public DbSet<Singleton> Singleton { get; set; }
        //...
    }
    ```
    ***

3. To create a singleton instance, override the `UpdateDatabaseAfterUpdateSchema` method of your module's `Updater` class:

    **File:** _SingletonSolution.Module\DatabaseUpdate\Updater.cs_

    # [EF Core](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.Data.Filtering;
    using DevExpress.Persistent.Base;
    using DevExpress.ExpressApp.Updating;
    using DevExpress.ExpressApp.EF;
    using DevExpress.Persistent.BaseImpl.EF;
    using SingletonSolution.Module.BusinessObjects;

    namespace SingletonSolution.Module.DatabaseUpdate;

    public class Updater : ModuleUpdater {
        public Updater(IObjectSpace objectSpace, Version currentDBVersion) :
            base(objectSpace, currentDBVersion) {
        }
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();
            if (ObjectSpace.GetObjectsCount(typeof(Singleton), null) == 0) {
                Singleton singleton = ObjectSpace.CreateObject<Singleton>();
                singleton.Name = "My Singleton";
                singleton.Description = "Sample Description";
            }
            ObjectSpace.CommitChanges();
        }
        public override void UpdateDatabaseBeforeUpdateSchema() {
            base.UpdateDatabaseBeforeUpdateSchema();
        }
    }
    ```

    # [XPO](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.Data.Filtering;
    using DevExpress.Persistent.Base;
    using DevExpress.ExpressApp.Updating;
    using DevExpress.Xpo;
    using DevExpress.ExpressApp.Xpo;
    using DevExpress.Persistent.BaseImpl;
    using SingletonSolution.Module.BusinessObjects;

    namespace SingletonSolution.Module.DatabaseUpdate;

    public class Updater : ModuleUpdater {
        public Updater(IObjectSpace objectSpace, Version currentDBVersion) :
            base(objectSpace, currentDBVersion) {
        }
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();
            if (ObjectSpace.GetObjectsCount(typeof(Singleton), null) == 0) {
                Singleton singleton = ObjectSpace.CreateObject<Singleton>();
                singleton.Name = "My Singleton";
                singleton.Description = "Sample Description";
            }
            ObjectSpace.CommitChanges();
        }
        public override void UpdateDatabaseBeforeUpdateSchema() {
            base.UpdateDatabaseBeforeUpdateSchema();
        }
    }
    ```
    # [VB.NET](#tab/tabid-vb-xpo)

    ```vb
    Imports DevExpress.ExpressApp
    Imports DevExpress.ExpressApp.Updating
    ' ...
    Public Class Updater
        Inherits ModuleUpdater
        ' ...
        Public Overrides Sub UpdateDatabaseAfterUpdateSchema()
            MyBase.UpdateDatabaseAfterUpdateSchema()
            If ObjectSpace.GetObjectsCount(GetType(Singleton), Nothing) = 0 Then
                Dim _singleton As Singleton = ObjectSpace.CreateObject(Of Singleton)()
                _singleton.Name = "My Singleton"
                _singleton.Description = "Sample Description"
            End If
            ObjectSpace.CommitChanges()
        End Sub
    End Class
    ```

    ***

> [!NOTE]
> XAF calls the `UpdateDatabaseAfterUpdateSchema` method each time the application runs in debugging mode. The method is targeted to create initial data when deploying the application or its update. To see an example of how you can use this method, refer to the following topic: [Supply Initial Data](xref:402985).

## Enable Access to a Singleton Detail View

This scenario details the following techniques to display a singleton object:
- Use a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) (recommended for occasional access)
- Add an item in the Main Form's navigation control (recommended for frequent access)

### Access Singleton Detail View in a Popup Window

The following code snippet creates the `ShowSingleton` Window Controller that contains a **PopupWindowShowAction** Action. This Action displays a popup window with the Singleton object's Detail View.

**File:** _SingletonSolution.Module\Controllers\ShowSingletonController.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using SingletonSolution.Module.BusinessObjects;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace SingletonSolution.Module.Controllers {
    public class ShowSingletonController : WindowController {
        public ShowSingletonController() {
            this.TargetWindowType = WindowType.Main;
            PopupWindowShowAction showSingletonAction =
                new PopupWindowShowAction(this, "ShowSingleton", PredefinedCategory.View);
            showSingletonAction.CustomizePopupWindowParams += showSingletonAction_CustomizePopupWindowParams;
        }
        private void showSingletonAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Singleton));
            DetailView detailView = Application.CreateDetailView(objectSpace, objectSpace.GetObjects<Singleton>()[0]);
            e.View = detailView;
        }
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports DevExpress.ExpressApp.Editors
' ...
Public Class ShowSingletonController
    Inherits WindowController
    Public Sub New()
        Me.TargetWindowType = WindowType.Main
        Dim showSingletonAction As New PopupWindowShowAction(Me, "ShowSingleton", PredefinedCategory.View)
        AddHandler showSingletonAction.CustomizePopupWindowParams, AddressOf showSingletonAction_CustomizePopupWindowParams
    End Sub
    Private Sub showSingletonAction_CustomizePopupWindowParams(ByVal sender As Object, ByVal e As CustomizePopupWindowParamsEventArgs)
        Dim objectSpace As IObjectSpace = Application.CreateObjectSpace(GetType(Singleton))
        Dim detailView As DetailView = Application.CreateDetailView(objectSpace, objectSpace.GetObjects(Of Singleton)()(0))
        detailView.ViewEditMode = ViewEditMode.Edit
        e.View = detailView
    End Sub
End Class
```

***

Run the application. Verify that the **Show Singleton** Action is available and you can modify the singleton.

Windows Forms
:   ![ShowSingletonActionWin](~/images/showsingletonactionwin116017.png)

ASP.NET Core Blazor  
:   ![ShowSingletonActionBlazor](~/images/ShowSingletonActionBlazor.png)

### Add an Item to the Navigation Control

Add the **NavigationItem** node to the [Application Model](xref:112580) using the [Model Editor](xref:112582) (see [Add an Item to the Navigation Control](xref:402131)). Set the **View** property of the newly added node to **Singleton_DetailView**.

![SingletonNavItemME](~/images/singletonnavitemme117137.png)

Run the application and verify that the singleton navigation item is available.

Windows Forms
:   ![SingletonNavItemWin](~/images/singletonnavitemwin117138.png)

ASP.NET Core Blazor
:   ![SingletonNavItemBlazor](~/images/SingletonNavItemBlazor.png)
