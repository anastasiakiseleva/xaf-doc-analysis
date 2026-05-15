---
uid: "112810"
seealso:
- linkId: "118592"
title: Read and Set Values for Built-in Application Model Nodes in Code
---
# Read and Set Values for Built-in Application Model Nodes in Code

The [Application Model](xref:112579) has a tree structure. You can iterate through the tree to access the required node. To access the root Application Model node, use the [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) property.

The following XAF classes also have the **Model** property to provide access to the corresponding node in the Application Model:

| Object | Property |
|---|---|
| [](xref:DevExpress.ExpressApp.XafApplication) | [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) |
| [](xref:DevExpress.ExpressApp.View) | [View.Model](xref:DevExpress.ExpressApp.View.Model) |
| [](xref:DevExpress.ExpressApp.Actions.ActionBase) | [ActionBase.Model](xref:DevExpress.ExpressApp.Actions.ActionBase.Model) |
| [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) | [PropertyEditor.Model](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Model) |

Application Model nodes implement the @DevExpress.ExpressApp.Model.IModelNode interface. You can use [IModelNode members](xref:DevExpress.ExpressApp.Model.IModelNode._members) to get parent and child nodes.

Application Model nodes also implement other interfaces with specific properties.
To access properties that are specific to a particular node, cast this node to one of the interfaces that it implements. For example, the root **Application** node implements the @DevExpress.ExpressApp.Model.IModelApplication node interface. You can cast this node to the @DevExpress.ExpressApp.Model.IModelApplication type and access the [IModelApplication.Logo](xref:DevExpress.ExpressApp.Model.IModelApplication.Logo) property. You can also cast the **Application** node to the @DevExpress.ExpressApp.SystemModule.IModelApplicationNavigationItems type and access the @DevExpress.ExpressApp.SystemModule.IModelApplicationNavigationItems.NavigationItems property. See the following topic for more information on available interfaces: [](xref:403535).
 ## Examples

The examples below make changes in the top layer of the Application Model (the user customization layer). Use the techniques from the following topic to customize the underlying zero layer: [](xref:112785).
 ### Customize a Root Application Node 

The following example accesses the root Application node and uses the [IModelRootNavigationItems.StartupNavigationItem](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.StartupNavigationItem) property to show the _Department_ListView_ View at application startup.

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp.SystemModule;  
using System.Linq;  
// ...  
    private void MainDemoWinApplication_LoggedOn(object sender, LogonEventArgs e) {  
        XafApplication app = (XafApplication)sender;  
        IModelApplicationNavigationItems navigationItems = (IModelApplicationNavigationItems)app.Model;  
        string targetViewId = "Department_ListView";  
        IModelNavigationItem targetNavigationItem = navigationItems.NavigationItems.AllItems.FirstOrDefault(
            item => item.View?.Id == targetViewId);
        if(targetNavigationItem != null) {  
            navigationItems.NavigationItems.StartupNavigationItem = targetNavigationItem;  
        }  
    }  
// ...  
```
 
# [VB.NET](#tab/tabid-vb)
 
```vb
Imports DevExpress.ExpressApp.SystemModule
Imports System.Linq
' ... 
    Private Sub MainDemoWinApplication_LoggedOn(ByVal sender As Object, ByVal e As LogonEventArgs)
        Dim app As XafApplication = CType(sender, XafApplication)
        Dim navigationItems As IModelApplicationNavigationItems = CType(app.Model, IModelApplicationNavigationItems)
        Dim targetViewId As String = "Department_ListView"
        Dim targetNavigationItem As IModelNavigationItem = navigationItems.NavigationItems.AllItems.FirstOrDefault(Function(item) item.View IsNot Nothing And item.View.Id = targetViewId)
        If targetNavigationItem IsNot Nothing Then
            navigationItems.NavigationItems.StartupNavigationItem = targetNavigationItem
        End If
    End Sub
' ...    
```
[`app.Model`]: xref:DevExpress.ExpressApp.XafApplication.Model
[`IModelApplicationNavigationItems`]: xref:DevExpress.ExpressApp.SystemModule.IModelApplicationNavigationItems
[`IModelNavigationItem`]: xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem

***

 ### Customize a Business Object Node 

The code below shows how to access the _Contact_ business class and change its [Caption](xref:DevExpress.ExpressApp.Model.IModelClass.Caption):

# [C#](#tab/tabid-csharp)

```csharp
using System.Linq;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;

namespace YourSolutionName.Module.Controllers {
    public class CustomController : ViewController {
        public CustomController() {
            var myAction1 = new SimpleAction(this, "MyAction1", null);
            myAction1.Execute += MyAction1_Execute;
        }

        private void MyAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
            var bo = Application.Model.BOModel.GetClass(typeof(Contact));
            if(bo != null) {
                var oldCaption = bo.Caption;
                bo.Caption = "New test caption";
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Linq
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Public Class CustomController
    Inherits ViewController
    Public Sub New()
        Dim myAction1 = New SimpleAction(Me, "MyAction1", String.Empty)
        AddHandler myAction1.Execute, AddressOf MyAction1_Execute
    End Sub
    Private Sub MyAction1_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim bo = Application.Model.BOModel.GetClass(GetType(Contact))
        If bo IsNot Nothing Then
            Dim oldCaption = bo.Caption
            bo.Caption = "New test caption"
        End If
    End Sub
End Class
```
[`GetClass`]: xref:DevExpress.ExpressApp.Model.IModelBOModel.GetClass(System.Type)
[`BOModel`]: xref:DevExpress.ExpressApp.Model.IModelApplication.BOModel
[`Application.Model`]: xref:DevExpress.ExpressApp.XafApplication.Model

***

## Limitations

The XAF UI does not reflect changes made in the Application Model after control creation. Customize the Application Model before the control used to display a target UI element is created and loaded. Access the control directly to customize a UI element after the control's creation. Refer to the following topic for more information: [](xref:402154).

You can also recreate the control with the latest Application Model changes as described in the following topic: [Apply Application Model Changes to the Current View Immediately](xref:118592).
