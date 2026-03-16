---
uid: DevExpress.Persistent.Base.DataSourceCriteriaAttribute.DataSourceCriteria
name: DataSourceCriteria
type: Property
summary: Returns criteria for filtering the List View displayed in a Lookup Property Editor or invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) Action in a popup window.
syntax:
  content: public string DataSourceCriteria { get; }
  parameters: []
  return:
    type: System.String
    description: A string value representing criteria for filtering the List View displayed in a Lookup Property Editor or invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) Action in a popup window.
seealso:
- linkId: "112612"
---
The common rules of writing a criteria are described in the [Ways to Build Criteria](xref:113052) topic. Note that you can use [Function Criteria Operators](xref:113307) and [Current Object Parameter](xref:113204) in your criteria.

You can change the criteria specified in code via the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's [IModelCommonMemberViewItem.DataSourceCriteria](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourceCriteria) property in the [Model Editor](xref:112830).

The example below demonstrates how you can use **DataSourceCriteria** to show Contacts that only have the Manager position in a [Lookup List View](xref:112611#list-view).

# [C#](#tab/tabid-csharp)
    
```csharp
using DevExpress.Persistent.Base;

// ...
public class Contact : Person {
    //...
    [DataSourceCriteria("Position.Title = 'Manager'")]
    public Contact Manager {
        // ...
    }
    // ...
}
```
***

For a complete scenario, see [](xref:402979).