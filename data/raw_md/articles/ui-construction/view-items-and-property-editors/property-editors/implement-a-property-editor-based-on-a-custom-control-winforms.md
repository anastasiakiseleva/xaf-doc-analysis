---
uid: "112679"
seealso:
- linkId: "113097"
title: 'Implement a Property Editor Based on a Custom Control (WinForms)'
owner: Ekaterina Kiseleva
---
# Implement a Property Editor Based on a Custom Control (WinForms)

This topic explains how to implement a Property Editor for WinForms applications. For demo purposes, the integer Property Editor based on the [NumericUpDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.numericupdown) control is implemented in this example.

> [!NOTE]
> * You can see the code implemented here in the **FeatureCenter** Demo, installed with **XAF**. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, by default.
> * If you intend to use a DevExpress WinForms control that is not integrated to XAF by default, refer to the [How to: Implement a Property Editor Using a DevExpress WinForms Control](xref:113015) topic.

Follow these steps to implement a WinForms Property Editor.

1. Inherit the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) or [](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor) class in the [WinForms application project](xref:118045) (_MySolution.Win_). [!include[PublicEditor](~/templates/publiceditor111797.md)]
2. Apply the [](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute) to specify the data type for which the Property Editor will be used (**Int32** in this example). If you pass **true** to the **PropertyEditor** attribute's last parameter, the Property Editor will be used for all integer properties in any business class.
3. Override the **CreateControlCore** method. In this method, instantiate, initialize and return the control instance (the [NumericUpDown](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.numericupdown) control in this example).
4. Determine which event of the control occurs when the editing value is changed by a user (e.g., the [NumericUpDown.ValueChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.numericupdown.valuechanged) event). Refer to the control's documentation to find the appropriate event. Subscribe to this event and call the **OnControlValueChanged** method (which internally raises the [PropertyEditor.ControlValueChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged) event) from the event handler.
5. Override the **Dispose** method and unsubscribe the event handled in the previous step.
6. Optionally, support the [](xref:DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport) interface and implement the [IInplaceEditSupport.CreateRepositoryItem](xref:DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport.CreateRepositoryItem) method. This step is only required if you are going to make the column editable in the editable List View.

The following code demonstrates **CustomIntegerEditor** class implementation based on the steps above.

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.XtraEditors.Repository;
// ...
[PropertyEditor(typeof(Int32), false)]
public class CustomIntegerEditor : PropertyEditor, IInplaceEditSupport {
    private NumericUpDown control = null;
    protected override void ReadValueCore() {
        if(control != null) {
            if(CurrentObject != null) {
                control.ReadOnly = false;
                control.Value = (int)PropertyValue;
            }
            else {
                control.ReadOnly = true;
                control.Value = 0;
            }
        }
    }
    private void control_ValueChanged(object sender, EventArgs e) {
        if(!IsValueReading) {
            OnControlValueChanged();
            WriteValueCore();
        }
    }
    protected override object CreateControlCore() {
        control = new NumericUpDown();
        control.Minimum = 0;
        control.Maximum = 5;
        control.ValueChanged += control_ValueChanged;
        return control;
    }
    protected override void OnControlCreated() {
        base.OnControlCreated();
        ReadValue();
    }
    public CustomIntegerEditor(Type objectType, IModelMemberViewItem info)
        : base(objectType, info) {
    }
    protected override void Dispose(bool disposing) {
        if(control != null) {
            control.ValueChanged -= control_ValueChanged;
            control = null;
        }
        base.Dispose(disposing);
    }
    RepositoryItem IInplaceEditSupport.CreateRepositoryItem() {
        RepositoryItemSpinEdit item = new RepositoryItemSpinEdit();
        item.MinValue = 0;
        item.MaxValue = 5;
        item.Mask.EditMask = "0";
        return item;
    }
    protected override object GetControlValueCore() {
        if(control != null) {
            return (int)control.Value;
        }
        return null;
    }
}
```
***

[!include[IComplexViewItem-note](~/templates/IComplexViewItem-note.md)]

To display a particular property using the **CustomIntegerEditor** Property Editor, customize the [Application Model](xref:112580). Invoke the [Model Editor](xref:112582) for the WinForms application project and navigate to the required **BOModel**| **Class**| **OwnMembers**| **Member** node. Set the node's [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property to **CustomIntegerEditor**. After this, the property specified by the Member node will be displayed by the **CustomIntegerEditor** in all [Views](xref:112611). To use a **CustomIntegerEditor** Property Editor in a specific Detail View only, use the **PropertyEditorType** property of the [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node instead.

> [!NOTE]
> [!include[IAppearanceFormat_Note](~/templates/iappearanceformat_note111897.md)]
