---
uid: DevExpress.Persistent.Base.ImageEditorAttribute.ListViewImageEditorMode
name: ListViewImageEditorMode
type: Property
summary: Specifies how images persisted by the target byte array property must be displayed in WinForms [List Views](xref:112611).
syntax:
  content: public ImageEditorMode ListViewImageEditorMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ImageEditorMode
    description: An [](xref:DevExpress.Persistent.Base.ImageEditorMode) enumeration value that specifies how images persisted by the target byte array property must be displayed in List Views. The default value is specified by the **ListViewImageEditorMode** property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node that is associated with the target byte array property.
seealso: []
---
Currently, the **PopupPictureEdit** mode is not supported in WinForms applications. If you select this mode, the image is displayed in a dropdown, analogously to the **DropDownPictureEdit** mode.