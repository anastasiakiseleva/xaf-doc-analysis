---
uid: DevExpress.Persistent.Base.General.ICategorizedItem
name: ICategorizedItem
type: Interface
summary: Declares members implemented by the classes that can be represented in a UI via the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor).
syntax:
  content: public interface ICategorizedItem
seealso:
- linkId: DevExpress.Persistent.Base.General.ICategorizedItem._members
  altText: ICategorizedItem Members
---
An object implementing the **ICategorizedItem** interface has an associated [ICategorizedItem.Category](xref:DevExpress.Persistent.Base.General.ICategorizedItem.Category). When the [TreeList Editors module](xref:112836) is added to the application, all the [List Views](xref:112611) that represent such objects are displayed via the **CategorizedListEditor**, by default.

To learn how to implement the **ICategorizedItem** interface, refer to the [Categorized List](xref:112838) topic.