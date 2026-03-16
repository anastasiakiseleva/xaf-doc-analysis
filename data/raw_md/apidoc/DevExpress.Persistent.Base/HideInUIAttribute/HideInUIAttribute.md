---
uid: DevExpress.Persistent.Base.HideInUIAttribute
name: HideInUIAttribute
type: Class
summary: Specifies whether a business class property or enumeration value is initially visible in certain areas of application UI.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true)]
    public class HideInUIAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.HideInUIAttribute._members
  altText: HideInUIAttribute Members
- linkId: "113679"
- linkId: "113285"
- linkId: "112817"
- linkId: "113680"
---

Some `HideInUIAttribute` options duplicate existing solutions that change property visibility in certain UI views:

| Existing solutions | HideInUiAttribute options |
|-|-|
| [`[Browsable(false)]`](xref:112701) | [`HideInUI.All`](xref:DevExpress.Persistent.Base.HideInUI.All) |
| [`[VisibleInListView(false)]`](xref:DevExpress.Persistent.Base.VisibleInListViewAttribute) | [`HideInUI.ListViewColumn`](xref:DevExpress.Persistent.Base.HideInUI.ListViewColumn) |
| [`[VisibleInLookupListView(false)]`](xref:DevExpress.Persistent.Base.VisibleInLookupListViewAttribute) | [`HideInUI.ListViewColumn`](xref:DevExpress.Persistent.Base.HideInUI.ListViewColumn) |
| [`[VisibleInDetailView(false)]`](xref:DevExpress.Persistent.Base.VisibleInDetailViewAttribute) | [`HideInUI.DetailViewEditor`](xref:DevExpress.Persistent.Base.HideInUI.DetailViewEditor) |
