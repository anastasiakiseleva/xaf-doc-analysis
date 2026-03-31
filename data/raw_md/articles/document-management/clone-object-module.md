---
uid: "112835"
seealso:
- linkId: DevExpress.ExpressApp.CloneObject.CloneObjectViewController
- linkId: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction
title: Clone Object (Copy Data Records)
---
# Clone Object (Copy Data Records)

The **Clone Object** module allows users to clone existing objects in a single click. This functionality can be useful when a user wants to create similar data items without the need to fill all the new data item's fields.

![Clone Object Module Winforms Blazor](~/images/cloneobject.png)

## Add the Clone Object Module to an App

The **Clone Object** module consists of a single assembly:
* _DevExpress.ExpressApp.CloneObject[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_

You can find it in the _DevExpress.ExpressApp.CloneObject_ NuGet package. 

 To enable the **Clone Object** module functionality in Windows Forms and ASP.NET Core Blazor applications, add [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectModule) to the [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) or [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) list:

**File:** _MySolution\CS\MySolution.Module\MySolutionModule.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.CloneObject;
// …
namespace MySolution.Module {
    public sealed partial class MySolutionModule : ModuleBase {
        public MySolutionModule() {
            // …
            RequiredModuleTypes.Add(typeof(CloneObjectModule));
        }
    }
}
```

[`RequiredModuleTypes`]: xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes
***

> [!TIP]
> * [!include[<@DevExpress.ExpressApp.ApplicationBuilder.ObjectCloningApplicationBuilderExtensions.AddCloning``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.CloneObject.ObjectCloningOptions})>,<ASP.NET Core Blazor/WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]
> * [!include[ExtraModulesNote1](~/templates/extramodulesnote1111180.md)]

## How It Works

The **Clone Object** module supplies the [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController). This Controller contains the **CloneObject Single Choice Action** that clones the selected object. 

The Action's `ChoiceActionBase.Items` collection includes the current object type and types inherited from the object's base class.

![|XAF CloneObject Action Items Collection, DevExpress](~/images/xaf-clone-common-base-object-devexpress.png)

> [!TIP]
> You can also clone incompatible types if they share the same interface. For more information, refer to the following section: [Clone Incompatible or Non-Assignable Object Types That Implement a Common Interface](xref:112835#clone-incompatible-or-non-assignable-object-types-that-implement-a-common-interface).

## Specify Object Types and Properties to Be Cloned

The **Clone Object** module extends the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** nodes with the [IModelClassCloneable.IsCloneable](xref:DevExpress.ExpressApp.CloneObject.IModelClassCloneable.IsCloneable) property. Set it to `True` to enable the action for objects of the selected type.

![XAF IsClonable Property in Model Editor, DevExpress](~/images/xaf-modeleditor-isclonable-property-devexpress.png)

Alternatively, decorate your business class with the following attribute in code: `[ModelDefault("IsCloneable", "True")]`.

The **CloneObject** Action is disabled if the current object has unsaved changes because the clone process works in a separate [Object Space](xref:113707). 

To prevent an individual field or property from being cloned, decorate it with [](xref:DevExpress.Persistent.Base.NonCloneableAttribute).

## Cloned Properties Behavior

| Property type | Cloning behavior | [XAF Blazor Main Demo](https://demos.devexpress.com/XAF/BlazorMainDemo/) example |
|-|-|-|
| Value (String, Boolean, Numeric, and so on) | Fully equivalent to the source object. | Clone an `Employee` object. All value type properties should be the same in the cloned object. |
| Reference | XAF clones the value of the reference property, but does not clone the referenced object. | Clone an `Employee` object. The `Position` property of both objects references the same `Position` object. |
| Aggregated reference | XAF clones the property value and the referenced object. | Clone an `Employee` object. The referenced `Address` object is also cloned. |
| Non-Aggregated Collection | The cloned collection is empty, if it is a part of an non-aggregated One-to-Many or Many-to-Many relationship or a weak/non-associated collection. | Clone a `Department` object that has a populated `Employee` collection. The cloned object's `Employee` collection is empty. |
| Aggregated collection | When you clone an object that has a populated aggregated collection, XAF also clones objects that populate this collection.  | Clone an `Employee` object. Objects from its `PhoneNumbers` collection are cloned too. |

## Clone Object Module Customization

To implement custom behavior for the `CloneObjectViewController` or **CloneObject** Action, use standard XAF techniques described in the following topics:
* [](xref:112676)
* [](xref:112728)

For example, you can use the following customization techniques: 

- Create a custom View Controller and override its `OnActivated` method to access the target Controller and its Action.
- Inherit from [CloneObjectViewController](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController) and override its own virtual methods. 

### Modify Default Cloner Logic or Implement a Fully Custom Algorithm

Handle the [CloneObjectViewController.CustomCloneObject](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomCloneObject) event to clone objects with custom logic.

[!include[customcloneobjectcodesnippet](~/templates/customcloneobjectcodesnippet.md)]

### Customize Display of a Cloned Object's Detail View

[!include[customshowclonedobjectcode](~/templates/customshowclonedobjectcode.md)]

### Prevent Cloning Descendants or Assignable Object Types

[!include[cloneobjectactionlimititemscollectioncode](~/templates/cloneobjectactionlimititemscollectioncode.md)]

### Clone Incompatible or Non-Assignable Object Types That Implement a Common Interface

To clone an object into an object of a different type, both types must be compatible: either they inherit one another or both inherit from the same type. If you want to clone incompatible types, you have to follow these steps:

1. Implement the same interface in both classes. For example, the following code snippets create `Note` and `Appointment` classes that both implement the `IText` interface:

    ```csharp
    using System.ComponentModel;
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;

    namespace YourApplicationName.Module.BusinessObjects;

    public interface IText {
        string Subject { get; set; }
        string Description { get; set; }
    }
    ```

    ```csharp
    using System.ComponentModel;
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;

    namespace YourApplicationName.Module.BusinessObjects;

    public class Note : BaseObject, IText {
        public virtual String Author { get; set; }
        public virtual string Subject { get; set; }
        public virtual string Description { get; set; }
    }
    ```

    ```csharp
    using System.ComponentModel;
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;

    namespace YourApplicationName.Module.BusinessObjects;

    public class Appointment : BaseObject, IText {
        public Appointment() { }
        public virtual String Organizer { get; set; }
        public virtual string Subject { get; set; }
        public virtual string Description { get; set; }
    }
    ```

2. Add the following controller to the application's **Module** project. This controller allows you to clone an `Appointment` object to either an `Appointment` or a `Note` object:

    ```csharp
    using DevExpress.ExpressApp.CloneObject;
    using DevExpress.XtraScheduler;
    using YourApplicationName.Module.BusinessObjects;

    namespace YourApplicationName.Module.Controllers;

    public class MyCloneObjectViewController : CloneObjectViewController {
        private void CloneObjectViewController_CustomGetCloneActionTargetTypes(object sender,
            CustomGetCloneActionTargetTypesEventArgs e) {
            if ((e.SourceType.Type == typeof(Note)) || (e.SourceType.Type == typeof(Appointment))) {
                e.TargetTypes.Add(Application.Model.BOModel[typeof(Note).FullName], typeof(Note));
                e.TargetTypes.Add(Application.Model.BOModel[typeof(Appointment).FullName], typeof(Appointment));
                e.Handled = true; }
        }
        public MyCloneObjectViewController() : base() {
                CustomGetCloneActionTargetTypes += CloneObjectViewController_CustomGetCloneActionTargetTypes; }
    }
    ```

    > [!NOTE]
    > When you clone a `Note` object into an `Apppointment` object, XAF copies the `Subject` and `Description` property values.

    ![XAF ASP.NET Core Blazor Clone Object to a Different Type, DevExpress](~/images/xaf-blazor-clone-object-different-types-devexpress.gif)
