---
uid: "113294"
seealso:
- linkId: "113010"
- linkId: "113218"
- linkId: "113345"
title: 'Test Validation Rules'
owner: Ekaterina Kiseleva
---
# Test Validation Rules

The [EasyTest](xref:113211) functional testing framework allows you to test validation rules.

To see step-by-step testing instructions for beginners, refer to the [Test an Action](xref:113218) topic.

Suppose you have an **Employee** business class, which declares the **Name** and **Age** properties. The properties have the following requirements:

- **Name.** Each **Employee** object must have a non-empty **Name**. To do this, apply the [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute) to the **Name** property. 
- **Age.** The **Age** value must be 18 or higher. Decorate the **Age** property with the [](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute). 

The following code snippet demonstrates how to apply these validation rules: 

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.Validation;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions,ImageName("BO_Employee")]
public class Employee : BaseObject {
    [RuleRequiredField("EmployeeIsAdult", DefaultContexts.Save)]
    public virtual string Name { get; set; }
    [RuleValueComparison("EmployeeNameIsRequired", DefaultContexts.Save, ValueComparisonType.GreaterThanOrEqual, 18)]
    public virtual int Age { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Persistent.Validation;
using DevExpress.Xpo;
// ...
[DefaultClassOptions, ImageName("BO_Employee")]
public class Employee : BaseObject {
    public Employee(Session session) : base(session) { }
    private string name;
    [RuleRequiredField("EmployeeIsAdult", DefaultContexts.Save)]
    public string Name {
        get => name;
        set => SetPropertyValue(nameof(Name), ref name, value);
    }
    private int age;
    [RuleValueComparison("EmployeeNameIsRequired", DefaultContexts.Save, ValueComparisonType.GreaterThanOrEqual, 18)]
    public int Age {
        get => age;
        set => SetPropertyValue(nameof(Age), ref age, value);
    }
}
```
***

## CheckValidationResult Command

In a Windows Forms application, the popup window is displayed when a validation error occurs. In a Blazor application, the validation results are displayed on the current page using the `ErrorInfoControl` (for more information, refer to the [](xref:112704) topic). To test all platforms in a single test script, you can use the [CheckValidationResult](xref:113208) EasyTest command. The image below illustrates the meaning of the command's parameters on WinForms platform:

![EasyTest_CheckValidationResult](~/images/easytest_checkvalidationresult116854.png)

To test the **Employee** object's validation rules, you can use the following EasyTest script.

# [ETS](#tab/tabid-ets)

```ETS
;#DropDB MySolutionEasyTest

#Application MySolutionWin
#Application MySolutionWeb
#Application MySolutionBlazor

;Create a new Employee:
*Action Navigation(Employee)
*Action New

;Save it with initial property values (empty Name and zero Age):
*Action Save

;Test the validation result that is displayed when saving:
*CheckValidationResult
 Message = Data Validation Error: *
 Info = "Name" must not be empty.
 Info = "Age" must be greater than or equal to "18".

;Close the error message:
#IfDef MySolutionWin
*Action Close
#EndIf

;Specify a valid Name and invalid Age:
*FillForm
 Name = Mary Tellitson
 Age = 17

;Save an Employee with invalid Age:
*Action Save

;Test the validation result that is displayed when saving:
*CheckValidationResult
 Message = Data Validation Error: *
 Info = "Age" must be greater than or equal to "18".


;Close the error message:
#IfDef MySolutionWin
*Action Close
#EndIf

;Specify a valid Age:
*FillForm
 Age = 18

;Save a valid Employee:
*Action Save

;Check that an error is not displayed:
!CheckValidationResult
 Message = ?*
```
***
