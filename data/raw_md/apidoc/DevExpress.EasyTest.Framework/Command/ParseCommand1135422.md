---
uid: DevExpress.EasyTest.Framework.Command.ParseCommand(DevExpress.EasyTest.Framework.CommandCreationParam)
name: ParseCommand(CommandCreationParam)
type: Method
summary: Parses the current command.
syntax:
  content: public virtual void ParseCommand(CommandCreationParam commandCreationParam)
  parameters:
  - id: commandCreationParam
    type: DevExpress.EasyTest.Framework.CommandCreationParam
    description: The **CommandCreationParam** object .
seealso:
- linkId: "113340"
---
Generally, you do not need to invoke this method from your code - it is used internally in the [TestExecutor Utility](xref:113210).

You can override this method in a custom command's implementation to perform custom activity after the command is parsed, for example, throw an exception when a mandatory parameter is omitted.