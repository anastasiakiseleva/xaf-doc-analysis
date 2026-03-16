---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.TryGetObjectHandle(System.Object,System.String@)
name: TryGetObjectHandle(Object, out String)
type: Method
summary: Creates a handle for the specified object if this object is persistent and is not a new one.
syntax:
  content: |-
    [Browsable(false)]
    public bool TryGetObjectHandle(object theObject, out string handle)
  parameters:
  - id: theObject
    type: System.Object
    description: An object for which a handle is created.
  - id: handle
    type: System.String
    description: A string that is the handle created for the specified object.
  return:
    type: System.Boolean
    description: '**true** if a handle has been created successfully for the specified object; otherwise **false**.'
seealso: []
---
This method is intended for internal use.