---
uid: DevExpress.EasyTest.Framework.Command.Parameters
name: Parameters
type: Property
summary: Gets parameters, passed to the [EasyTest](xref:113211) command.
syntax:
  content: public ParameterList Parameters { get; }
  parameters: []
  return:
    type: DevExpress.EasyTest.Framework.ParameterList
    description: A [](xref:DevExpress.EasyTest.Framework.ParameterList) object that exposes parameters of the EasyTest command.
seealso: []
---
An EasyTest command can have a primary parameter and several secondary parameters. Additionally, an extra parameter can be passed as the primary parameter's argument. An example of using this property is provided in the [How to: Implement a Custom EasyTest Command](xref:113340) topic. For the complete description of EasyTest syntax, refer to the [EasyTest Script Reference](xref:113208) topic.
