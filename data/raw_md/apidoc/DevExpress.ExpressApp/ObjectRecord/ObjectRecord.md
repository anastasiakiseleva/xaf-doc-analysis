---
uid: DevExpress.ExpressApp.ObjectRecord
name: ObjectRecord
type: Class
summary: Contains information to get the wrapped object's value or to load the complete business object from a database in [InstantFeedback, InstantFeedbackView, or ServerView](xref:118450) mode.
syntax:
  content: 'public class ObjectRecord : IObjectRecord'
seealso:
- linkId: DevExpress.ExpressApp.ObjectRecord._members
  altText: ObjectRecord Members
---
The [ListView.CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject) and [ListView.SelectedObjects](xref:DevExpress.ExpressApp.ListView.SelectedObjects) properties return **ObjectRecord** objects instead of original business objects when the List View operates in the **InstantFeedback**, **InstantFeedbackView**, or **ServerView** mode.