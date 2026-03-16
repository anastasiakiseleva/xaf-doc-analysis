---
uid: DevExpress.ExpressApp.Editors.ViewItem
name: ViewItem
type: Class
summary: Represents a base class for [View Items](xref:112612).
syntax:
  content: 'public abstract class ViewItem : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.Editors.ViewItem._members
  altText: ViewItem Members
- linkId: "112816"
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
---
The `ViewItem` class implements basic functionality for items that can be contained in a [Detail View](xref:112611). This functionality includes:

* The capability to display View Items via a specified control in a UI. Basically, a Detail View's representation in a UI is a set of controls that display View Items.
    
    See the following members: [ViewItem.Control](xref:DevExpress.ExpressApp.Editors.ViewItem.Control), [ViewItem.CreateControl](xref:DevExpress.ExpressApp.Editors.ViewItem.CreateControl), [ViewItem.ControlCreating](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreating) and [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated).
* A View Item can be related to the object that the parent Detail View presents. For instance, the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor), being the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class' descendant, represents the properties of the object presented by the Detail View.
    
    See the [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) and [ViewItem.ObjectType](xref:DevExpress.ExpressApp.Editors.ViewItem.ObjectType).
* A View Item can be refreshed when the parent Detail View is refreshed. Refreshing is assumed to be data related.
    
    See [ViewItem.Refresh](xref:DevExpress.ExpressApp.Editors.ViewItem.Refresh*).
* The capability to save the current settings of the control to the [Application Model](xref:112580), so that the next time the control is created the same settings are used.
    
    See [ViewItem.SaveModel](xref:DevExpress.ExpressApp.Editors.ViewItem.SaveModel).

To access the Detail View in which a View Item is contained, use the [ViewItem.View](xref:DevExpress.ExpressApp.Editors.ViewItem.View) property.

XAF ships with the following descendants of the `ViewItem` class:

* [](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem)
    
    Displays an [Action Container](xref:112610) specified by the [IModelActionContainerViewItem.ActionContainer](xref:DevExpress.ExpressApp.Model.IModelActionContainerViewItem.ActionContainer) property of the [Application Model](xref:112580)'s corresponding ActionContainerViewItem node. Used to display [Actions](xref:112622) on a Detail View layout.
* [](xref:DevExpress.ExpressApp.Layout.ControlViewItem)
    
    Displays a control specified by the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property of the [Application Model](xref:112580)'s corresponding **ControlDetailItem** node. Use it to specify a control that will be displayed in a UI. In ASP.NET Core Blazor, `DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem` is a descendant that can also display any parameter-less [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/).
* [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)
    
    Displays a [View](xref:112611) in a nested [Frame](xref:112608). Used to display several Views side-by-side on a Dashboard View.
* [](xref:DevExpress.ExpressApp.Editors.PropertyEditor)
    
    Displays a control bound to a property of the current View's object. There are multiple property editor types in the **XAF**. They are intended for different data types, and therefore use different controls.
* [](xref:DevExpress.ExpressApp.Editors.StaticImage)
    
    Displays an image.
* [](xref:DevExpress.ExpressApp.Editors.StaticText)
    
    Displays a label.

To implement a custom View Item, inherit from the **ViewItem** class. The following protected members that are not described in the documentation can be overridden:

| Member | Description |
|---|---|
| `CreateControlCore` | Called by the [ViewItem.CreateControl](xref:DevExpress.ExpressApp.Editors.ViewItem.CreateControl) method. You should return the control that will represent your View Item in a UI. |
| `SaveModelCore` | Called by the [ViewItem.SaveModel](xref:DevExpress.ExpressApp.Editors.ViewItem.SaveModel) method. You can override it to save the settings of a View Item and its control to the Application Model. This allows display of the View Item in the same manner as it was before it was recreated. |
| `Dispose` | Called by the [ViewItem.Dispose](xref:DevExpress.ExpressApp.Editors.ViewItem.Dispose) method. Override it if you need to dispose custom allocated resources. |
| `OnCurrentObjectChanging` and `OnCurrentObjectChanged` | Called when the [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) property is changed. |
| `OnControlCreating` and `OnControlCreated` | Called when a control (see [ViewItem.Control](xref:DevExpress.ExpressApp.Editors.ViewItem.Control)) is created. Raise the [ViewItem.ControlCreating](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreating) and [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) events. |

> [!NOTE]
> A custom View Item should be implemented in a platform-specific [application project](xref:118045) and decorated with the [](xref:DevExpress.ExpressApp.Editors.ViewItemAttribute). This View Item will be loaded to the Application Model, which means that you will be able to use it in a UI. 

For details on View Items and basics on how to implement custom ones, refer to the [View Items](xref:112612) and [How to: Implement a View Item](xref:405483) topics.

To access a View Item of the View for which a [Controller](xref:112621) is activated, handle the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) events, as it is demonstrated in the following article: [](xref:402153).
