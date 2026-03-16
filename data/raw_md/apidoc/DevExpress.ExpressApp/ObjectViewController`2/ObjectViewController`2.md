---
uid: DevExpress.ExpressApp.ObjectViewController`2
name: ObjectViewController<ViewType, ObjectType>
type: Class
summary: A base class for [View Controllers](xref:112621) intended for Object Views.
syntax:
  content: 'public abstract class ObjectViewController<ViewType, ObjectType> : ViewController<ViewType> where ViewType : ObjectView'
  typeParameters:
  - id: ViewType
    description: Specifies the [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) value.
  - id: ObjectType
    description: Specifies the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) value
seealso:
- linkId: DevExpress.ExpressApp.ObjectViewController`2._members
  altText: ObjectViewController<ViewType, ObjectType> Members
---
This Controller inherist from the [](xref:DevExpress.ExpressApp.ObjectViewController) and introduces two generic type parameters:

| Parameter | Description |
|-|-|
| `ViewType` | Specifies the [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) value. |
| `ObjectType` | Specifies the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) value. |

Use this class as the base class for a custom Controller to ensure that the custom Controller is activated for a specific View type and Object type.

The following code snippet demonstrates a custom View Controller derived from the generic `ObjectViewController`.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Blazor.Server.Controllers;

public sealed class ContactListViewController : ObjectViewController<ListView, Contact> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is DxGridListEditor gridListEditor) {
            // ...
        }
    }
}
```
***

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

Visual Studio designer cannot be used with generic components, so you cannot use it to design generic Controllers. As a possible workaround, you can declare an intermediate non-generic base class, derived from a generic Controller and decorated with the [DesignerCategoryAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.designercategoryattribute), and then derive your custom Controller from this intermediate class. The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel;
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Blazor.Server.Controllers;

public abstract class MyIntermediateListViewController : ObjectViewController<ListView, Contact> {
    // ...
}

public sealed class MyViewController : MyIntermediateListViewController {
    // ...
}
```
***
