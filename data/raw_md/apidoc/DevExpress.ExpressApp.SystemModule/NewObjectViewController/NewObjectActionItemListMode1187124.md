---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectActionItemListMode
name: NewObjectActionItemListMode
type: Property
summary: Specifies the mode for populating the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) items list.
syntax:
  content: |-
    [DefaultValue(NewObjectActionItemListMode.Default)]
    public NewObjectActionItemListMode NewObjectActionItemListMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.NewObjectActionItemListMode
    description: An [](xref:DevExpress.ExpressApp.SystemModule.NewObjectActionItemListMode) enumeration value specifying the mode for populating the New Action's items list.
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t326296/how-to-remove-or-hide-the-base-class-from-the-new-action-s-items-list
  altText: How to remove or hide the base class from the New Action's items list
---
Use the following code to change the **NewObjectActionItemListMode** value in a specific View.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.Persistent.BaseImpl;
// ...
public class CustomizeNewActionItemsListController : ObjectViewController<ObjectView, Task> {
    protected override void OnActivated() {
        base.OnActivated();
        NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.NewObjectActionItemListMode = NewObjectActionItemListMode.LastDescendantsOnly;
        } 
    }
}
```
***

To specify the default value applied in all Views, use the static [NewObjectViewController.DefaultNewObjectActionItemListMode](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.DefaultNewObjectActionItemListMode) field.

The **NewObjectActionItemListMode** value is ignored in a case when there are no descendants of the current business object type. In the **ExcludeBaseType** and **LastDescendantsOnly** modes, the New Action may become inactive if it is impossible to instantiate any of the descendants (e.g., due to the [Security System](xref:113366) restrictions).

If the modes listed in the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectActionItemListMode) enumeration do not fit your requirements, handle the [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) and [NewObjectViewController.CollectCreatableItemTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes) events instead of using the **NewObjectActionItemListMode** property. An example is provided in the [How to: Customize the New Action's Items List](xref:112915) topic.
