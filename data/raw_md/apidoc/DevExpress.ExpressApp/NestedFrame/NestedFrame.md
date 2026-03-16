---
uid: DevExpress.ExpressApp.NestedFrame
name: NestedFrame
type: Class
summary: Serves as a site for [Views](xref:112611) displayed by [View Items](xref:112612).
syntax:
  content: 'public class NestedFrame : Frame'
seealso:
- linkId: DevExpress.ExpressApp.NestedFrame._members
  altText: NestedFrame Members
- linkId: "112607"
- linkId: "112608"
- linkId: "112611"
- linkId: "112609"
---
Nested Frames are used by [View Items](xref:112612) that display [Views](xref:112611), such as the [DetailPropertyEditor](xref:113572). Compared to the base [](xref:DevExpress.ExpressApp.Frame) class, **NestedFrame** introduces a single [NestedFrame.ViewItem](xref:DevExpress.ExpressApp.NestedFrame.ViewItem) property that provides access to the [View Item](xref:112612) that uses the [](xref:DevExpress.ExpressApp.NestedFrame). You can use this property to access the parent View and its object from a context, where you have access to the nested Frame.

For general details on Frames, refer to the [](xref:DevExpress.ExpressApp.Frame) class description and the [Windows and Frames](xref:112608) help topic.