---
uid: DevExpress.Persistent.Base.VisibleInLookupListViewAttribute
name: VisibleInLookupListViewAttribute
type: Class
summary: Specifies whether the column that corresponds to the target business class property is initially visible in a Lookup Property Editor's [List View](xref:112611).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true)]
    public class VisibleInLookupListViewAttribute : ModelExportedBoolValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.VisibleInLookupListViewAttribute._members
  altText: VisibleInLookupListViewAttribute Members
- linkId: DevExpress.Persistent.Base.VisibleInListViewAttribute
- linkId: "113679"
- linkId: "113285"
---
By default, an `Object` type business class property is displayed via a Lookup Property Editor. In the drop-down frame of this Property Editor, there is a List View that displays a collection of existing objects of the specified type.

![LookupPropetyEditors_1](~/images/lookuppropetyeditors_1115398.png)

By default, a Lookup Property Editor's List View displays the properties that use the [](xref:DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute) and/or `DefaultProperty` attribute. However, you can display any business class property in that List View by applying the `VisibleInLookupListView` attribute to this property, and passing `true` as the attribute's `value` parameter. If the business class has no default property, all its properties are visible in a Lookup List View. In this case, you can hide a certain property by applying the `VisibleInLookupListView` attribute to this property, and passing `false` as the attribute's `value` parameter. To learn more about the rules used to generate the default columns set in List Views, refer to the [List View Column Generation](xref:113285) topic.

The value passed as the `VisibleInLookupListView` attribute's _value_ parameter is set for the read-only [IModelMember.IsVisibleInLookupListView](xref:DevExpress.ExpressApp.Model.IModelMember.IsVisibleInLookupListView) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. Use the [Model Editor](xref:112582) to see whether a particular property is visible in a Lookup List View.
