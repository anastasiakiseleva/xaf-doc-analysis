---
uid: DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute
name: CriteriaOptionsAttribute
type: Class
summary: Indicates that the target string property stores a filter criterion.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property)]
    public class CriteriaOptionsAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute._members
  altText: CriteriaOptionsAttribute Members
---
To use this attribute, add a property of the `System.Type` type to your business class. This property should return a type whose objects are filtered by the filter criterion. Pass this property's name to the attribute's `objectTypeMemberName` parameter.

For more information about the use of `CriteriaOptionsAttribute`, refer to the following topics:

- [How to: Use Criteria Property Editors](xref:113143)
- [](xref:113578)
- [](xref:113565)

This attribute sets the `PropertyEditorType` property of the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelMember) node to the following values:

DevExpress.ExpressApp.Blazor.Editors.FilterPropertyEditor
:   In ASP.NET Core Blazor applications
DevExpress.ExpressApp.Win.Editors.CriteriaPropertyEditor
:   In Windows Forms applications with `UseAdvancedFilterEditorControl` = `DefaultBoolean.False`
DevExpress.ExpressApp.Win.Editors.AdvancedCriteriaPropertyEditor
:   In Windows Forms applications with `UseAdvancedFilterEditorControl` = `DefaultBoolean.True` or `DefaultBoolean.Default`

You can specify another value in the [Model Editor](xref:112582).

For additional information about Property Editors for filter properties, refer to the following help topic: [](xref:113564).
