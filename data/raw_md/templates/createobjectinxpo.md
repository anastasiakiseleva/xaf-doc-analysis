The following code snippet demonstrates how to initialize **Employee**'s **Address1** and **Manager** reference properties with new and existing objects:

**File**: _MySolution.Module\BusinessObjects\Employee.cs_

# [C#](#tab/tabid-csharp)

```csharp{<:0:>}
using DevExpress.Data.Filtering;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
public class Employee : Person {
    //...
    public override void AfterConstruction() {
        base.AfterConstruction();
        Address1 = new Address(Session);
        Address1.Country = Session.FindObject<Country>(CriteriaOperator.Parse("Name = 'USA'"));
        if(Address1.Country == null) {
            Address1.Country = new Country(Session);
            Address1.Country.Name = "USA";
        }
        Manager = Session.FindObject<Employee>(CriteriaOperator.Parse(
            "FirstName = 'John' && LastName = 'Doe'"));
    }
}
```
***