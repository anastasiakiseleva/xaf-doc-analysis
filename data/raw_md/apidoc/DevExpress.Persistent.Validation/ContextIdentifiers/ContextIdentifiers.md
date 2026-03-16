---
uid: DevExpress.Persistent.Validation.ContextIdentifiers
name: ContextIdentifiers
type: Struct
summary: Identifies [Validation Contexts](xref:113008).
syntax:
  content: 'public struct ContextIdentifiers : IList<string>, ICollection<string>, IEnumerable<string>, IEnumerable, IEquatable<ContextIdentifiers>'
seealso:
- linkId: DevExpress.Persistent.Validation.ContextIdentifiers._members
  altText: ContextIdentifiers Members
- linkId: "113684"
---
A **ContextIdentifiers** wraps a set of validation contexts and provides methods to compare different **ContextIdentifiers**. The **ContextIdentifiers** type is used in various built-in classes, and you may need to occasionally instantiate it and pass instances to methods and properties of built-in XAF classes. To create a **ContextIdentifiers** for given validation contexts, use the [ContextIdentifiers](xref:DevExpress.Persistent.Validation.ContextIdentifiers.#ctor*) constructor, and pass a list of the required validation contexts as the _identifiers_ parameter.