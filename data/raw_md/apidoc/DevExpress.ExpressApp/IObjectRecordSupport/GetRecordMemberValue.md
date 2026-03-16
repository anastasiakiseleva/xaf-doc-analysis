---
uid: DevExpress.ExpressApp.IObjectRecordSupport.GetRecordMemberValue(DevExpress.ExpressApp.ObjectRecord,System.String)
name: GetRecordMemberValue(ObjectRecord, String)
type: Method
summary: Returns the value of the wrapped object's member. Use this method to get this value without loading a real object.
syntax:
  content: object GetRecordMemberValue(ObjectRecord objectRecord, string memberName)
  parameters:
  - id: objectRecord
    type: DevExpress.ExpressApp.ObjectRecord
    description: A wrapper of a business object whose member's value this method returns.
  - id: memberName
    type: System.String
    description: A member whose value this method returns.
  return:
    type: System.Object
    description: The value of the wrapped object's member.
seealso: []
---
Refer to the [How to: Access Objects Selected in the Current View](xref:113324#access-currently-selected-objects-when-an-action-is-executed) topic to see an example.