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

# [VB.NET](#tab/tabid-vb)

```vb{<:1:>}
Imports DevExpress.Data.Filtering
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.Xpo
' ...
Public Class Employee
    Inherits Person
    '...
    Public Overrides Sub AfterConstruction()
        MyBase.AfterConstruction()
        Address1 = New Address(Session)
        Address1.Country = Session.FindObject(Of Country)(CriteriaOperator.Parse("Name = 'USA'"))
        If Address1.Country Is Nothing Then
            Address1.Country = New Country(Session)
            Address1.Country.Name = "USA"
            Address1.Country.Save()
        End If
        Manager = Session.FindObject(Of Employee)(CriteriaOperator.Parse( _
        "FirstName = 'John' && LastName = 'Doe'"))
    End Sub
End Class
```

***