---
uid: DevExpress.ExpressApp.Editors.PropertyEditor
name: PropertyEditor
type: Class
summary: A base class for Property Editors.
syntax:
  content: 'public abstract class PropertyEditor : ViewItem, IAppearanceEnabled, IAppearanceBase, IAppearanceVisibility, INotifyAppearanceVisibilityChanged, IDisposable, IServiceProviderClient'
seealso:
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor._members
  altText: PropertyEditor Members
- linkId: "113097"
- linkId: "112679"
- linkId: "402189"
- linkId: DevExpress.ExpressApp.Editors.PropertyEditorAttribute
---
Implements base functionality for [Property Editors](xref:113097):

* The control that represents a Property Editor in a UI can read and write the value of the bound property.
    
    Related members:
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ReadValue)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.WriteValue)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStoring)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueRead)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Refresh)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyValue)
    
* The Property Editor derives information on the property it represents using the [PropertyEditor.MemberInfo](xref:DevExpress.ExpressApp.Editors.PropertyEditor.MemberInfo) property.
    
    See also [PropertyEditor.PropertyName](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyName).
* Members that affect the way the properties are displayed in the Property Editor's control:
    
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.IsPassword)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.MaxLength)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.IsCaptionVisible)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ImmediatePostData)
    - [](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Caption).



`PropertyEditor` descendants extend its functionality according to a property's type and the UI platform (Windows Forms and ASP.NET Core Blazor): [Data Types Supported by built-in Editors](xref:113014).


The `PropertyEditor` class and its descendants can be used to implement custom Property Editors. For details, see the [Implement Custom Property Editors](xref:113097) topic. 
When deriving from the `PropertyEditor` class, the following protected members, not described in the documentation, can be overridden:

| Member | Description |
|---|---|
| OnValueStoring | Called in the [PropertyEditor.WriteValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.WriteValue) method, before the value specified in a Property Editor's control is set for the bound property. Raises the [PropertyEditor.ValueStoring](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStoring) event. Note that the `WriteValue` method is not called in the built-in Windows Forms Property Editors, because they support `Binding` (see System.Windows.Forms.Binding in MSDN). If you implement a Property Editor that supports binding, call the `OnValueStoring` method, where required. |
| OnValueStored | Called in the [PropertyEditor.WriteValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.WriteValue) method, after the value specified in a Property Editor's control has been set for the bound property. Raises the [PropertyEditor.ValueStored](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored) event. Note that the `WriteValue` method is not called in the built-in Windows Forms Property Editors, because they support `Binding` (see System.Windows.Forms.Binding in MSDN). If you implement a Property Editor that supports binding, call the `OnValueStored` method, where required. |
| OnControlValueChanged | Raises the [PropertyEditor.ControlValueChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged) event. However, the `OnControlValueChanged` method is not called by default. You should call it in your `PropertyEditor` class' descendants, after the control's value has been changed. For details, refer to the event's description. |
| WriteValueCore | Called in the [PropertyEditor.WriteValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.WriteValue) method. Passes the value from the control to the property (from [PropertyEditor.ControlValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue) to [PropertyEditor.PropertyValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyValue)). Override this method to implement custom code. Note that the `WriteValue` method is not called in the built-in Windows Forms Property Editors, because they support binding (see System.Windows.Forms.Binding in MSDN). So, do not override the `WriteValueCore` method in descendants of these Property Editors. |
| OnValueRead | Called in the [PropertyEditor.ReadValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ReadValue) method, after the value of the bound property is set for the control's value. |
| ReadValueCore | Called as a result of calling the [PropertyEditor.ReadValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ReadValue) method. Since it is abstract, override it to add the code that passes the value from the property to a control (from [PropertyEditor.PropertyValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyValue)  to [PropertyEditor.ControlValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue)). |
| CanReadValue | Returns `true` if the Property Editor's control is created. Override this method to provide extra conditions to determine whether the property's value can be read to the control's value. |
| OnAllowEditChanged | Called after the Property Editor's read-only state has been changed (see [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit)). Raises the [PropertyEditor.AllowEditChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEditChanged) event. |
| IsMemberSetterRequired | Returns whether the Property Editor requires a property with a set accessor to allow editing. For most Property Editor types, override this method to return `true`. However, for certain Property Editors, such as Property Editors that deal with reference properties, this method must return `false` to allow editing of the referenced object's properties. |
| GetControlValueCore | This method is abstract. Override it to perform the code that gets the value of the Property Editor's control. |

A constructor of a custom Property Editor must be implemented in the following manner.

# [C#](#tab/tabid-csharp)

```csharp
public MyPropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
```
***

The _model_ parameter is required for the factory that creates all View Items, including Property Editors for a Detail View.

> [!NOTE]
> A custom Property Editor should be implemented in a platform-specific [application project](xref:118045). This Property Editor will be loaded into the Application Model, which means that you will be able to use it in a UI. 

Typical implementation of the `PropertyEditor` class' descendant comprises the following steps:

1. Override the `CreateControlCore` method. Create and return an instance of the required control. Subscribe to the control's `ValueChanged` event to call the `WriteValue` method.
2. Override the `GetControlValueCore` method. Return the value specified by the control.
3. Override the `ReadValueCore` method. Assign the Property Editor's `PropertyValue` to the control's binding property.

The `PropertyEditor` class exposes the basic Property Editor functionality. When implementing a custom Property Editor, use one of the derived classes.

If you implement a Property Editor, use the [](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute).

To access a Property Editor of the View for which a [Controller](xref:112621) is activated, handle the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) events, as demonstrated in the following article: [](xref:402153).

The `PropertyEditor` class implements the [](xref:DevExpress.ExpressApp.Editors.IAppearanceVisibility) and [](xref:DevExpress.ExpressApp.Editors.IAppearanceEnabled) interfaces so that the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) can change the visibility or enabled state of a property to which a [conditional appearance rule](xref:113286) is applied.

It is recommended to place your control customization code to the `SetupControl` method when you create custom property editor.