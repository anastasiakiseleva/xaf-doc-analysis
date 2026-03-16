---
uid: DevExpress.ExpressApp.DC.DomainComponentAttribute
name: DomainComponentAttribute
type: Class
summary: Specifies that a target class should be registered in the [types info subsystem](xref:113224) and should affect [Application Model](xref:112580) construction.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = true)]
    public class DomainComponentAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.DomainComponentAttribute._members
  altText: DomainComponentAttribute Members
---
Participation in generation of the Application Model means that the **BOModel** node will expose a child node corresponding to the **DomainComponentAttribute** target. The **Views** node will contain **ListView** and **DetailView** nodes for the **DomainComponentAttribute** target.

You do not need to use the **DomainComponentAttribute** attribute in the following cases:

* The target is an XPO persistent class declared within an XAF module.
* The target is an Entity Framework class registered in a DbContext which is declared within an XAF module.

These classes are collected and registered automatically.

However, the **DomainComponentAttribute**  is required when you declare a [non-persistent class](xref:116516) and want to display Views of this class in a UI.
