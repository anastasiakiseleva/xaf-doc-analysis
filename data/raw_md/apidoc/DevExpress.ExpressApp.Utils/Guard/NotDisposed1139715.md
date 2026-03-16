---
uid: DevExpress.ExpressApp.Utils.Guard.NotDisposed(DevExpress.ExpressApp.IDisposableExt,System.String[])
name: NotDisposed(IDisposableExt, String[])
type: Method
summary: Ensures that a specific object has not been disposed of.
syntax:
  content: public static void NotDisposed(IDisposableExt obj, params string[] exceptionDataEntries)
  parameters:
  - id: obj
    type: DevExpress.ExpressApp.IDisposableExt
    description: An **IDisposableExt** object to check.
  - id: exceptionDataEntries
    type: System.String[]
    description: An array of strings specifying exception data entries.
seealso: []
---
If the specified object has been disposed of, an exception is thrown.