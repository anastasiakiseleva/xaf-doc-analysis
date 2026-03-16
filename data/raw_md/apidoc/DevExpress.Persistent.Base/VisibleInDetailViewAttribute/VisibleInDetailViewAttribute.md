---
uid: DevExpress.Persistent.Base.VisibleInDetailViewAttribute
name: VisibleInDetailViewAttribute
type: Class
summary: Specifies whether the View Item that corresponds to the target business class property is visible in a Detail View.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true)]
    public class VisibleInDetailViewAttribute : ModelExportedBoolValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.VisibleInDetailViewAttribute._members
  altText: VisibleInDetailViewAttribute Members
---

> [!TIP]
> Use the [`HideInUI.DetailViewEditor`](xref:DevExpress.Persistent.Base.HideInUI.DetailViewEditor) attribute instead.

If you want a particular property of a business class to not be visible in a Detail View that displays objects of this class, apply the **VisibleInDetailView** attribute to this  property, and pass **false** as the attribute's _value_ parameter. In this instance, a [!include[Node_Views_DetailView_Layout](~/templates/node_views_detailview_layout111385.md)] | **LayoutItem** node will not be generated for this property in the Application Model. If you do not apply this attribute, a View Item will be generated and arranged according to the XAF internal layout rules (see [View Items Layout Customization](xref:112817)).

The value passed as the **VisibleInDetailView** attribute's _value_ parameter, is assigned to the read-only [IModelMember.IsVisibleInDetailView](xref:DevExpress.ExpressApp.Model.IModelMember.IsVisibleInDetailView) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. Use the [Model Editor](xref:112582), to see whether a particular property is visible in a Detail View.

> [!NOTE]
> By default, the value which is passed as the **VisibleInListView** attribute's _value_ parameter remains in descendants of the target property's class.