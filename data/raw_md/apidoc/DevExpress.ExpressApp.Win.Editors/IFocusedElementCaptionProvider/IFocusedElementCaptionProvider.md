---
uid: DevExpress.ExpressApp.Win.Editors.IFocusedElementCaptionProvider
name: IFocusedElementCaptionProvider
type: Interface
summary: Implemented by Windows Forms [List Editors](xref:113189) that support copying contents of the focused cell to the clipboard.
syntax:
  content: public interface IFocusedElementCaptionProvider
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.IFocusedElementCaptionProvider._members
  altText: IFocusedElementCaptionProvider Members
---
The Windows Forms [ListViewFocusedElementToClipboardController](xref:113141) provides the **CopyCellValue** [Action](xref:112622). This Action copies the contents of the focused cell to the clipboard and is available in pop-up menus of List Editors implementing the **IFocusedElementCaptionProvider** interface. The interface exposes a single [IFocusedElementCaptionProvider.FocusedElementCaption](xref:DevExpress.ExpressApp.Win.Editors.IFocusedElementCaptionProvider.FocusedElementCaption) property. When implementing a custom Windows Forms List Editor, return the textual representation of the focused cell contents via this property.