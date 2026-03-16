---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin
name: IModelOptionsWin
type: Interface
summary: Used to extend the [Application Model](xref:112580)'s **Options** node with the properties required in Windows Forms applications.
syntax:
  content: |-
    [RuleCriteria("[UIType] != ##Enum#DevExpress.ExpressApp.UIType,StandardMDI# Or [FormStyle] != ##Enum#DevExpress.XtraBars.Ribbon.RibbonFormStyle,Ribbon#", UsedProperties = "UIType,FormStyle", CustomMessageTemplate = "The combination of UIType = 'StandardMDI' and FormStyle = 'Ribbon' settings is not supported. Please change one of these settings to proceed.")]
    public interface IModelOptionsWin : IModelNode, IModelAsync
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin._members
  altText: IModelOptionsWin Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. The **IModelOptionsWin** is used by the **SystemWindowsFormsModule** module, to extend the [](xref:DevExpress.ExpressApp.Model.IModelOptions). 