---
uid: DevExpress.Persistent.Validation.ContextIdentifier
name: ContextIdentifier
type: Struct
summary: Identifies a [Validation Context](xref:113008).
syntax:
  content: 'public struct ContextIdentifier : IComparable, IEquatable<ContextIdentifier>'
seealso:
- linkId: DevExpress.Persistent.Validation.ContextIdentifier._members
  altText: ContextIdentifier Members
- linkId: "113684"
---
**ContextIdentifier**s wrap validation contexts and provide methods to compare and sort them. The **ContextIdentifier** type is used in various built-in classes, and you may need to occasionally instantiate it and pass instances to methods and properties of built-in XAF classes. To create a **ContextIdentifier** for a given validation context, use the [ContextIdentifier](xref:DevExpress.Persistent.Validation.ContextIdentifier.#ctor(System.String)) constructor and pass the validation context as the _id_ parameter.