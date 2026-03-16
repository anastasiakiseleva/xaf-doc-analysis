---
uid: DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourcePropertyIsNullCriteria
name: DataSourcePropertyIsNullCriteria
type: Property
summary: Indicates criteria for filtering the List View of the target property's Lookup Property Editor, in case the [DataSourcePropertyAttribute.DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty) is not specified.
syntax:
  content: public string DataSourcePropertyIsNullCriteria { get; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents criteria for filtering the List View of the target property's Lookup Property Editor.
seealso: []
---
You can change the criteria specified in code via the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's [IModelCommonMemberViewItem.DataSourcePropertyIsNullCriteria](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourcePropertyIsNullCriteria) property in the [Model Editor](xref:112830).

To learn how to specify criteria via the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute), refer to the [](xref:112681) topic. The common rules of writing a criteria are described in the [Ways to Build Criteria](xref:113052) topic. Additionally, you can use [Function Criteria Operators](xref:113307) as well as the [Current Object Parameter](xref:113204) in the criteria.