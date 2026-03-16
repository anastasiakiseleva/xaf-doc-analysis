---
uid: DevExpress.ExpressApp.DC.OptimisticLockAttribute
name: OptimisticLockAttribute
type: Class
summary: Applies to EF Core business class properties. Specifies [concurrency options](xref:405384).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, Inherited = true)]
    public class OptimisticLockAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.OptimisticLockAttribute._members
  altText: OptimisticLockAttribute Members
---
Use `OptimisticLockAttribute` to specify concurrency control options in a business class of an EF Core-based XAF application.

The following code snippet uses `OptimisticLockAttribute`:

[!include[](~/templates/optimisticlockattribute.md)]

For more information about optimistic concurrency control in EF Core-based XAF applications, refer to the following help topic: [](xref:405384).
