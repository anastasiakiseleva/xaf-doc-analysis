---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction
name: CloneObjectAction
type: Property
summary: Gets a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) Action used to clone persistent objects.
syntax:
  content: public SingleChoiceAction CloneObjectAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: An Action used to clone persistent objects.
seealso: []
---

This [Action](xref:112622) enables you to create a clone of the current object as an object of the current type (it requires a single object to be selected). You can clone:
- an object currently selected in a List View
- a Detail View's current object.

It invokes a Detail View with a new object. Property values of this object are copied from the object that has been cloned. To prohibit copying a specific property value, apply the [](xref:DevExpress.Persistent.Base.NonCloneableAttribute) attribute to it.

To activate the **CloneObject** Action for the List and Detail [Views](xref:112611) of an object type, navigate to the [Application Model](xref:112580) and set the object type's [IModelClassCloneable.IsCloneable](xref:DevExpress.ExpressApp.CloneObject.IModelClassCloneable.IsCloneable) property to `true`.

![XAF Clone Object Module in Windows Forms and ASP.NET Core Blazor, DevExpress](~/images/cloneobject.png)

In addition, you can create an object of the class inherited from the current object's base class. For this purpose, set the base class' [IModelClassCloneable.IsCloneable](xref:DevExpress.ExpressApp.CloneObject.IModelClassCloneable.IsCloneable) property to `true`. 

To change the **CloneObjectAction**'s behavior, create a custom View Controller, override the `OnActivated` method, and access the [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController) Controller and its Action.

[!include[cloneobjectactionlimititemscollectioncode](~/templates/cloneobjectactionlimititemscollectioncode.md)]

The **CloneObject** Action is disabled when there are unsaved changes in the current object because the clone process works in a separate Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)). To change this behavior, set the [CloneObjectViewController.AllowCloneWhenModified](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.AllowCloneWhenModified) property to `true`.

> [!NOTE]
> The `CloneObjectViewController` adds a handler to the [BaseObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanged) event of the `View.ObjectSpace` object.  This handler updates the Action's [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property by the "NotModified" key according to `AllowCloneWhenModified` and [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified) values. The "NotModified" key name is defined by the [CloneObjectViewController.IsNotModifiedEnabledKey](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.IsNotModifiedEnabledKey) constant.

To determine why the **CloneObject** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information about the **CloneObject** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).