---
uid: "113684"
seealso: []
title: Validation (Prevent Data Errors)
---
# Validation (Prevent Data Errors)

Different tasks in business applications often require information that is to be edited to meet special requirements. Sometimes end-user actions may not meet these requirements. Consider a simple example where an end-user fills out a form with personal information. It is usually necessary to fill out all the required fields, but the end-user may be unaware of this.  Special notifications should be provided to ensure that all required data is entered.  Another example relates to the internal business logic of an application. For example, a rule may require that the total sum of an order not exceed a certain value.

Validation Rules like these should be controlled by the application, so that end-users are unable to enter invalid data. Sometimes, you may need to change the rules according to your requirements. If you implemented your rules with custom code, you will need to change your code and re-build the application. At the same time, this approach does not let administrators change Validation Rules. To avoid these problems, XAF provides a special **Validation** module. This module allows for the easy and effective control of user input. This topic details the basic concepts of this tool. To learn how to use it to provide data validation in your application, refer to the [Declare Validation Rules](xref:113251) topic.

## Contextual Validation Concept
XAF uses the following validation concept. Restrictions can be applied to business classes and their properties. For example, filling in a particular property is required when saving an object, or the value of a certain property must be within 10 and 20 (also checked when saving an object). For these requirements, **IsRequiredField** and **Range** are the **Rules**, and that moment the **Rules** (e.g., object saving) are checked is called the **Context**. Thus, [Validation Rules](xref:113008) and [Validation Contexts](xref:113685) are the main concepts of the Validation system.

## Validation in UI
Validation is organized in the UI with the [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController) that manages the adjustment of rules. Thus, it is possible to specify whether objects with a particular property value need to be validated, modify a collection of aggregated objects or a collection of all objects to be validated in particular context. For additional technical information, refer to this controller description.

## Validation System Elements
The [Validation Module](xref:113684) comprises three assemblies.

* _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_
	
	Contains base validation-specific classes and services. This assembly represents a module, since it contains the [](xref:DevExpress.ExpressApp.Validation.ValidationModule) class - a descendant of the [](xref:DevExpress.ExpressApp.ModuleBase) class. This module also uses entities from the _DevExpress.Persistent.Base.v<:xx.x:>.dll_ assembly, which is referenced by default: base classes and interfaces, common Validation Rules implementation and static validation services that are used to collect Validation Rules and check objects.

* _DevExpress.ExpressApp.Validation.Win.v<:xx.x:>.dll_
	
	Implements WinForms-specific validation functionality. This assembly is a module, since it contains the [](xref:DevExpress.ExpressApp.Validation.Win.ValidationWindowsFormsModule) class - a descendant of the **ModuleBase** class. This module creates validation error messages (invoked after rules are broken) that are more informative and user friendly than default exception messages. Additionally, this module provides in-place validation support (see [IModelValidationContext.AllowInplaceValidation](xref:DevExpress.ExpressApp.Validation.IModelValidationContext.AllowInplaceValidation)).

* _DevExpress.ExpressApp.Validation.Blazor.v<:xx.x:>.dll_
	
	Implements ASP.NET Core Blazor-specific validation functionality. This assembly is a module, since it contains the **DevExpress.ExpressApp.Validation.Blazor.ValidationBlazorModule** class - a descendant of the **ModuleBase** class. This module creates validation error messages (invoked after rules are broken) that are more informative and user friendly than default exception messages.

## Add Validation Module to an XAF Application

[!include[ExtraModulesNote](~/templates/extramodulesnote11181.md)]
* [!include[<@DevExpress.ExpressApp.Blazor.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions}) / @DevExpress.ExpressApp.Win.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions})>,<ASP.NET Core Blazor / WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

[!include[<Validation Module>](~/templates/main-demo-tip.md)]