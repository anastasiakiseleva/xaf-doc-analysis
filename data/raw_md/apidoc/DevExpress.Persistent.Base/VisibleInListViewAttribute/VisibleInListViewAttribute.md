---
uid: DevExpress.Persistent.Base.VisibleInListViewAttribute
name: VisibleInListViewAttribute
type: Class
summary: Specifies whether the column that corresponds to the target business class property is initially visible in a [List View](xref:112611).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true)]
    public class VisibleInListViewAttribute : ModelExportedBoolValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.VisibleInListViewAttribute._members
  altText: VisibleInListViewAttribute Members
- linkId: "113679"
- linkId: "113285"
---

> [!TIP]
> Use the [`HideInUI.ListViewColumn`](xref:DevExpress.Persistent.Base.HideInUI.ListViewColumn) attribute instead.

If you want to customize the default process of [list view columns generation](xref:113285) and make a particular property of a business class initially visible in the List View that displays objects of this class, apply the **VisibleInListView** attribute to this property and pass **true** as the attribute's _value_ parameter. If you do not want a property to be visible in the List View, apply this attribute and pass **false** as the _value_ parameter.

The value passed as the **VisibleInListView** attribute's _value_ parameter, is set for the read-only [IModelMember.IsVisibleInListView](xref:DevExpress.ExpressApp.Model.IModelMember.IsVisibleInListView) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. Use the [Model Editor](xref:112582) to see whether a particular property is visible in a List View.

> [!NOTE]
> An end-user can change a column's visibility via the **Column Chooser**, if the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) is used to display the List View.

> [!NOTE]
> By default, the value which is passed as the **VisibleInListView** attribute's _value_ parameter remains in descendants of the target property's class.