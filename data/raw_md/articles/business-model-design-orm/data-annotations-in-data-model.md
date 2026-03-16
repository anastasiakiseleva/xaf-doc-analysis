---
uid: "112701"
seealso:
- linkType: HRef
  linkId: "https://learn.microsoft.com/en-us/dotnet/standard/attributes/applying-attributes"
  altText: Applying Attributes
- linkId: "112580"
title: Data Annotation Attributes
---
# Data Annotation Attributes

You can apply attributes to a business class or its members to specify information necessary to generate your XAF application. The attributes can specify validation rules, how the data is displayed, set relationships between classes, and so on. This topic supplies a list of attributes that can be applied in an XAF application.

## Built-in XAF Attributes

Attribute | Description
---------|----------
 @DevExpress.Persistent.Base.ActionAttribute | [!summary-include(DevExpress.Persistent.Base.ActionAttribute)]
 @DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute | [!summary-include(DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute)]
 @DevExpress.ExpressApp.DC.AggregatedAttribute | [!summary-include(DevExpress.ExpressApp.DC.AggregatedAttribute)]
 @DevExpress.ExpressApp.DC.CalculatedAttribute | [!summary-include(DevExpress.ExpressApp.DC.CalculatedAttribute)]
 @DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute | [!summary-include(DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute)]
 @DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute | [!summary-include(DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute)]
 @DevExpress.Persistent.Validation.CodeRuleAttribute | [!summary-include(DevExpress.Persistent.Validation.CodeRuleAttribute)]
 @DevExpress.ExpressApp.CollectionSourceModeAttribute | [!summary-include(DevExpress.ExpressApp.CollectionSourceModeAttribute)]
 @DevExpress.Persistent.Base.CreatableItemAttribute | [!summary-include(DevExpress.Persistent.Base.CreatableItemAttribute)]
 @DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute | [!summary-include(DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute)]
 @DevExpress.Persistent.Base.DataSourceCriteriaAttribute | [!summary-include(DevExpress.Persistent.Base.DataSourceCriteriaAttribute)]
 @DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute | [!summary-include(DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute)]
 @DevExpress.Persistent.Base.DataSourcePropertyAttribute | [!summary-include(DevExpress.Persistent.Base.DataSourcePropertyAttribute)]
 @DevExpress.Persistent.Base.DefaultClassOptionsAttribute | [!summary-include(DevExpress.Persistent.Base.DefaultClassOptionsAttribute)]
 @DevExpress.ExpressApp.DefaultListViewOptionsAttribute | [!summary-include(DevExpress.ExpressApp.DefaultListViewOptionsAttribute)]
 @DevExpress.ExpressApp.Model.DetailViewLayoutAttribute | [!summary-include(DevExpress.ExpressApp.Model.DetailViewLayoutAttribute)]
 @DevExpress.ExpressApp.DC.DomainComponentAttribute | [!summary-include(DevExpress.ExpressApp.DC.DomainComponentAttribute)]
 @DevExpress.Persistent.Base.ExpandObjectMembersAttribute | [!summary-include(DevExpress.Persistent.Base.ExpandObjectMembersAttribute)]
 @DevExpress.ExpressApp.DC.FieldSizeAttribute | [!summary-include(DevExpress.ExpressApp.DC.FieldSizeAttribute)]
 @DevExpress.Persistent.Base.FileAttachmentAttribute | [!summary-include(DevExpress.Persistent.Base.FileAttachmentAttribute)]
 @DevExpress.Persistent.Base.FileTypeFilterAttribute | [!summary-include(DevExpress.Persistent.Base.FileTypeFilterAttribute)]
 @DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute | [!summary-include(DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute)]
 @DevExpress.Persistent.Base.HideInUIAttribute | [!summary-include(DevExpress.Persistent.Base.HideInUIAttribute)]
 @DevExpress.Persistent.Base.ImageEditorAttribute | [!summary-include(DevExpress.Persistent.Base.ImageEditorAttribute)]
 @DevExpress.Persistent.Base.ImageNameAttribute | [!summary-include(DevExpress.Persistent.Base.ImageNameAttribute)]
 @DevExpress.Persistent.Base.ImagesForBoolValuesAttribute | [!summary-include(DevExpress.Persistent.Base.ImagesForBoolValuesAttribute)]
 @DevExpress.Persistent.Base.ImmediatePostDataAttribute | [!summary-include(DevExpress.Persistent.Base.ImmediatePostDataAttribute)]
 @DevExpress.Persistent.Base.IndexAttribute | [!summary-include(DevExpress.Persistent.Base.IndexAttribute)]
 @DevExpress.ExpressApp.Data.KeyAttribute | [!summary-include(DevExpress.ExpressApp.Data.KeyAttribute)]
 @DevExpress.ExpressApp.Editors.ListEditorAttribute | [!summary-include(DevExpress.ExpressApp.Editors.ListEditorAttribute)]
 @DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute | [!summary-include(DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute)]
 @DevExpress.Persistent.Base.LookupEditorModeAttribute | [!summary-include(DevExpress.Persistent.Base.LookupEditorModeAttribute)]
 @DevExpress.ExpressApp.Model.ModelDefaultAttribute | [!summary-include(DevExpress.ExpressApp.Model.ModelDefaultAttribute)]
 @DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute | [!summary-include(DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute)]
 @DevExpress.Persistent.Base.NavigationItemAttribute | [!summary-include(DevExpress.Persistent.Base.NavigationItemAttribute)]
 @DevExpress.Persistent.Base.NonCloneableAttribute | [!summary-include(DevExpress.Persistent.Base.NonCloneableAttribute)]
 @DevExpress.Persistent.Base.NotClonedInfoAttribute | [!summary-include(DevExpress.Persistent.Base.NotClonedInfoAttribute)]
 @DevExpress.Persistent.Base.ObjectCaptionFormatAttribute | [!summary-include(DevExpress.Persistent.Base.ObjectCaptionFormatAttribute)]
 @DevExpress.ExpressApp.DC.OptimisticLockAttribute  | [!summary-include(DevExpress.ExpressApp.DC.OptimisticLockAttribute)]
 @DevExpress.ExpressApp.Editors.PropertyEditorAttribute | [!summary-include(DevExpress.ExpressApp.Editors.PropertyEditorAttribute)]
 @DevExpress.Persistent.Validation.RuleBaseAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleBaseAttribute)]
 @DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute)]
 @DevExpress.Persistent.Validation.RuleCriteriaAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleCriteriaAttribute)]
 @DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute)]
 @DevExpress.Persistent.Validation.RuleIsReferencedAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleIsReferencedAttribute)]
 @DevExpress.Persistent.Validation.RuleObjectExistsAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleObjectExistsAttribute)]
 @DevExpress.Persistent.Validation.RuleRangeAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleRangeAttribute)]
 @DevExpress.Persistent.Validation.RuleRegularExpressionAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleRegularExpressionAttribute)]
 @DevExpress.Persistent.Validation.RuleRequiredFieldAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleRequiredFieldAttribute)]
 @DevExpress.Persistent.Validation.RuleStringComparisonAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleStringComparisonAttribute)]
 @DevExpress.Persistent.Validation.RuleUniqueValueAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleUniqueValueAttribute)]
 @DevExpress.Persistent.Validation.RuleValueComparisonAttribute | [!summary-include(DevExpress.Persistent.Validation.RuleValueComparisonAttribute)]
 @DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute | [!summary-include(DevExpress.ExpressApp.Filtering.SearchClassOptionsAttribute)]
 @DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute | [!summary-include(DevExpress.ExpressApp.Filtering.SearchMemberOptionsAttribute)]
 @DevExpress.ExpressApp.Security.SecurityBrowsableAttribute | [!summary-include(DevExpress.ExpressApp.Security.SecurityBrowsableAttribute)]
 @DevExpress.Persistent.Base.ToolTipAttribute | [!summary-include(DevExpress.Persistent.Base.ToolTipAttribute)]
 @DevExpress.ExpressApp.Editors.ViewItemAttribute | [!summary-include(DevExpress.ExpressApp.Editors.ViewItemAttribute)]
 @DevExpress.Persistent.Base.VisibleInReportsAttribute | [!summary-include(DevExpress.Persistent.Base.VisibleInReportsAttribute)]
 @DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute | [!summary-include(DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute)]
 @DevExpress.ExpressApp.DC.XafDisplayNameAttribute | [!summary-include(DevExpress.ExpressApp.DC.XafDisplayNameAttribute)]

## XPO Attributes

The following table lists attributes from the @DevExpress.Xpo namespace specifically used by XAF. The remaining built-in XPO attributes are processed only by XPO.

{|
|-

! Attribute
! Description
|-

| @DevExpress.Xpo.AggregatedAttribute
| Indicates that a property or field references other aggregated persistent objects. When this attribute is applied to a collection property, it must be accompanied by the @DevExpress.Xpo.AssociationAttribute.

In XAF, objects from aggregated collections are retrieved by the `XPNestedObjectSpace` (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)). If an aggregated collection is a part of the One-To-Many relationship, the **Link** and **Unlink** Actions are not available, but the **New** Action is added to populate the collection.

Aggregated objects are meant to be created and managed only in the context of a master object, since they are considered a part of it. When XAF generates the default [Detail View](xref:112611) for an aggregated child object, a [Property Editor](xref:112612) corresponding to the associated master object is not included in the layout. To override this behavior, first, invoke the [Model Editor](xref:112582) for the required **Views** | **Detail View** node's **Items** child node. Add a **PropertyEditor** child node using the context menu for the property that is the owning class. Second, add the newly declared Property Editor to the Detail View's layout (see [View Items Layout Customization](xref:112817)).

For details on how to set relationships with aggregated collections, refer to [Relationships Between Persistent Objects in Code and UI](xref:112654).
|-

| @DevExpress.Xpo.KeyAttribute
| Indicates that a property or a field is a key. Key properties (fields) can be read-only in XAF applications.

Key property values are used to correctly identify and distinguish between different instances of a business class. Usually, key properties are read-only and autogenerated.
|-

| @DevExpress.Xpo.MemberDesignTimeVisibilityAttribute
| Specifies whether to make the target business class or member visible in the Application Model or not. If you pass **false** as the attribute's parameter, you will not see the target class/member in the Model Editor or in the UI.

Properties are persisted, even when they are hidden using this attribute.
|-

| @DevExpress.Xpo.DisplayNameAttribute
| Specifies a caption for the target enumeration value.

Specifically, this attribute's value is assigned to the [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) property of Application Model's **Localization** | **Enums** | **Enum** | **EnumerationValue** node.
|-

| @DevExpress.Xpo.SizeAttribute
| Specifies the maximum number of characters that can be stored in a column created to store the data of the target string type property. If this attribute is not applied, a string property can be set to a value consisting of a maximum of 100 characters.

Note that this attribute only specifies the database column size. The attribute does not prevent users from entering more than the specified number of characters using Property Editors. For instance, suppose you have a string property decorated with the Size attribute that specifies that the corresponding database column's size must be 10. If a custom Property Editor used to visualize the property allows users to enter more characters, it is perfectly valid for them to do so. In this instance, a SQL exception will be raised when trying to save an object. To ensure that users will not be able to enter and save more than a fixed maximum number of characters, use the [Validation Module](xref:113684). For example, you can decorate a business class with @DevExpress.Persistent.Validation.RuleCriteriaAttribute, and use the **Len** [function operator](xref:4928) to enforce the maximum length for a string property.

In XAF, the value passed as the attribute's parameter is set as a maximum length for Windows Forms `RichTextPropertyEditor`.

In fact, this attribute can be applied to any property type. This will influence the visibility of the corresponding List View column. If the @DevExpress.Persistent.Base.VisibleInListViewAttribute and @DevExpress.Xpo.DelayedAttribute are not applied to a target property and the **SizeAttribute**'s parameter passes a value that is more than 255 (for example, SizeAttribute.Unlimited), the corresponding column is set invisible by default.

This attribute's value is assigned to the [IModelMember.Size](xref:DevExpress.ExpressApp.Model.IModelMember.Size) property of the Application Model's **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node.
|}
