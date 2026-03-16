---
uid: DevExpress.Persistent.Base.ImageEditorAttribute.DetailViewImageEditorMode
name: DetailViewImageEditorMode
type: Property
summary: Specifies how images persisted by the target byte array property must be displayed in WinForms [Detail Views](xref:112611).
syntax:
  content: public ImageEditorMode DetailViewImageEditorMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ImageEditorMode
    description: An [](xref:DevExpress.Persistent.Base.ImageEditorMode) enumeration value that specifies how images represented by the target byte array property must be displayed in Detail Views. The default value is specified by the [IModelMember.DetailViewImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorMode) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node, that represents the target **Image** property.
seealso: []
---
Currently, the **PopupPictureEdit** mode is not supported in WinForms applications. If you select this mode, the image is displayed in a dropdown, analogously to the **DropDownPictureEdit** mode.