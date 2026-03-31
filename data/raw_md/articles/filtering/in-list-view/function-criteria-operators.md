---
uid: "113307"
seealso:
- linkId: "113480"
- linkId: "404016"
title: Function Criteria Operators
---
# Function Criteria Operators

The **XAF** includes various techniques to filter List Views: [at the data source level](xref:112988), [in the Application Model](xref:112992), and with special methods for filtering Lookup Property Editor List Views. In each technique, you may need to set static variables as filter criteria values. For example, the filter "Task.DueDate must be set to the current date" needs the CurrentDate variable (calculated each time it is required). For this purpose, use Function Criteria Operators, which represent functions that return a specific value (such as the current date or the current user) or the result of handling the specified arguments (such as the concatenation function). This topic describes Function Criteria Operators, shows how to use them when filtering, and explains how to implement Custom Function Operators.

## Function Criteria Operators Basics
Function Criteria Operators are a part of the [criteria language](xref:4928). In criteria strings, a Function Criteria Operator name should be followed by brackets containing operands that represent function arguments, or empty brackets if it does not take arguments. The following criterion demonstrates how to use the **LocalDateTimeToday** Operator:

``[Task.DueDate] = LocalDateTimeToday()``

Multiple Function Criteria Operators, such as **LocalDateTimeAfterTomorrow** or **Replace**, are available out of the box. Refer to the [](xref:DevExpress.Data.Filtering.FunctionOperatorType) help topic for a complete list. The following table lists the XAF-specific Function Criteria Operators available in XAF applications:

{|
|-

! Operator
! Description
! Examples
|-

| **CurrentUserId()**
| Returns the current user's identifier. This custom Function Criteria Operator is registered in the [](xref:DevExpress.ExpressApp.SystemModule.SystemModule)'s [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method override. This Operator's **Evaluate** method returns the @DevExpress.ExpressApp.SecuritySystem.CurrentUserId property value.
| ``User.Oid = CurrentUserId()``
|-

| **CurrentTenantId()**
| Returns the current [tenant](xref:404436)'s identifier. This custom Function Criteria Operator is registered in the [](xref:DevExpress.ExpressApp.SystemModule.SystemModule)'s [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method override. The **Evaluate** method is not supported for this function: the function is intended to be called from a [CriteriaOperator](xref:DevExpress.Data.Filtering.CriteriaOperator), where its call is automatically replaced with the correct ID value.
| ``TenantId = CurrentTenantId()``
|-

| **IsCurrentUserId(userId)**
| Returns **True** if the current user has the specified identifier. This custom Function Criteria Operator is registered in the [](xref:DevExpress.ExpressApp.SystemModule.SystemModule)'s [ModuleBase.CustomizeTypesInfo](xref:DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method override. The Operator's **Evaluate** method compares the specified identifier with the @DevExpress.ExpressApp.SecuritySystem.CurrentUserId property value. In WinForms applications, you can choose **IsCurrentUserId** in the [Excel-inspired](xref:1425) column's filter dropdown and in the [Filter Editor](xref:2471).
| ``IsCurrentUserId(Oid)``
|-

| **IsCurrentUserInRole(roleName)**
| Determines whether the currently logged on user is assigned to a specified role. Returns false when no user is currently logged on. The [](xref:DevExpress.ExpressApp.Security.SecurityModule) registers this custom Function Criteria Operator in the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event handler if **SecuritySystem.CurrentUser** implements the **IUserWithRoles** or [](xref:DevExpress.ExpressApp.Security.ISecurityUserWithRoles) interfaces. This Operator's **Evaluate** method casts the **SecuritySystem.CurrentUser** property value to the **IUserWithRoles** and **ISecurityUserWithRoles** interfaces and checks that the **Roles** collection contains the specified role.
| ``IsCurrentUserInRole('Admin')``
|-

| **IsNewObject(obj)**
| Indicates whether a specified object has been created but not saved to the database. This operator gets the current [Object Space](xref:113707) using the static [BaseObjectSpace.FindObjectSpaceByObject](xref:DevExpress.ExpressApp.BaseObjectSpace.FindObjectSpaceByObject(System.Object)) method and then returns the [IObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.IObjectSpace.IsNewObject(System.Object)) result, and returns **false** if the Object Space is not found. You can use this Operator on the client-side only; do not use it in security permissions criteria. This operator supports persistent classes and non-persistent classes that implement the @DevExpress.ExpressApp.IObjectSpaceLink interface.
| ``IsNewObject(This)``
``IsNewObject(Manager)``
|}

## Important Remark on the DateTime Function Criteria Operators
The **DateTime** parameters do not support addition and subtraction operations. The following expression is incorrect:

``[Task.DueDate] > (LocalDateTimeToday() - 3) AND [Task.DueDate] < (LocalDateTimeToday() + 3)``

To add or subtract values from the **DateTime** parameters, use the **DateTime** management functions the **XPO** exposes, such as **AddDays** and **AddYears**. 
For instance, this is the correct way to write the previous criterion:

``[Task.DueDate] > ADDDAYS(LocalDateTimeToday(), -3) AND [Task.DueDate] < ADDDAYS(LocalDateTimeToday(), 3)``

For a complete list of functions with descriptions, refer to the [Criteria Language Syntax](xref:4928) help topic.

> [!NOTE]
> **DateTime** parameters support plain addition and subtraction operations in certain database management systems (DBMS) – there are no errors when such an expression is evaluated on the server side. For example, when filtering a [List View](xref:112611) with the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute), the criterion is processed on the server. If the server supports addition and subtraction operations for **DateTime** parameters (for example, Microsoft SQL Server or Microsoft Jet Database Engine), the criterion is correctly processed.
