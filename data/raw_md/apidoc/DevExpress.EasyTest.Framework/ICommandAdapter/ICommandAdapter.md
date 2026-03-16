---
uid: DevExpress.EasyTest.Framework.ICommandAdapter
name: ICommandAdapter
type: Interface
summary: Declares members exposed by [EasyTest](xref:113211) command adapters.
syntax:
  content: public interface ICommandAdapter
seealso:
- linkId: DevExpress.EasyTest.Framework.ICommandAdapter._members
  altText: ICommandAdapter Members
---
Generally, you do not need to implement this interface. It is implemented by built-in command adapters in the _DevExpress.ExpressApp.EasyTest.WinAdapter.v<:xx.x:>.dll_ and _DevExpress.ExpressApp.EasyTest.BlazorAdapter.v<:xx.x:>.dll_ assemblies. An instance of `ICommandAdapter` object is passed to the `InternalExecute` method of the [](xref:DevExpress.EasyTest.Framework.Command) class, so you can use the [ICommandAdapter.CreateTestControl](xref:DevExpress.EasyTest.Framework.ICommandAdapter.CreateTestControl(System.String,System.String)) method when [implementing a custom EasyTest command](xref:113340).
