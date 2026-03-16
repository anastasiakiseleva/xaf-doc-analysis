---
uid: DevExpress.Persistent.Base.General.ITreeNode
name: ITreeNode
type: Interface
summary: Declares members implemented by the classes that can be represented in a UI via the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor).
syntax:
  content: public interface ITreeNode
seealso:
- linkId: DevExpress.Persistent.Base.General.ITreeNode._members
  altText: ITreeNode Members
- linkId: DevExpress.Persistent.Base.General.ITreeNodeImageProvider
---
An object implementing the **ITreeNode** interface represents a tree node. When the [TreeList Editors module](xref:112836) is added to the application, all the [List Views](xref:112611) that represent such objects are displayed via the **TreeListEditor**, by default.

To learn how to implement the **ITreeNode** interface, refer to the [Display a Tree List using the ITreeNode Interface](xref:112837) topic.

To support tree node images in a class implementing the **ITreeNode** interface, implement the [](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider) interface.