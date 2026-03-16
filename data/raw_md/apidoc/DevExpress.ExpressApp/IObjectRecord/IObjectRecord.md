---
uid: DevExpress.ExpressApp.IObjectRecord
name: IObjectRecord
type: Interface
summary: The interface for business object wrappers that XAF uses in different [List View data access modes](xref:113683).
syntax:
  content: public interface IObjectRecord
seealso:
- linkId: DevExpress.ExpressApp.IObjectRecord._members
  altText: IObjectRecord Members
---
This interface is implemented by the following classes XAF uses to wrap business objects in different [List View data access modes](xref:113683):

{|
|-
! Wrapper
! Data access mode
|-

| @DevExpress.ExpressApp.ObjectRecord
| [ServerView, InstantFeedback, and InstantFeedbackView](xref:118450)
|-

| @DevExpress.ExpressApp.XafDataViewRecord
| [DataView](xref:118452)
|}

Use this interface when determining if this object the @DevExpress.ExpressApp.View.CurrentObject or @DevExpress.ExpressApp.View.SelectedObjects property returns is a real business object or a wrapper. Refer to the [How to: Access Objects Selected in the Current View](xref:113324#access-currently-selected-objects-when-an-action-is-executed) topic to see an example.