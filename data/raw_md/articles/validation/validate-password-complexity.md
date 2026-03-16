---
uid: "401909"
title: Validate Password Complexity
seealso:
  - linkId: "113251"
  - linkId: "112649"
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/xaf-how-to-enforce-password-complexity-in-xaf
    altText: 'GitHub Example: XAF - How to enforce password complexity'
---
# Validate Password Complexity
The **ChangePasswordByUser** Action is accessible by end users when the [Standard Authentication](xref:119064#standard-authentication) type is used in an **XAF** application. By default, end users have the ability to change their passwords and set simple or even empty passwords. However, the production environment can have strict security, and it may therefore be required to use only complex passwords. The solution is to validate a new password value when an end user attempts to change a password.

The **Change My Password** dialog contains the **ChangePasswordParameters** Detail View.

![Tutorial_SS_Lesson1_3](~/images/tutorial_ss_lesson1_3115531.png)

The **NewPassword** is a property to be validated. As this property is implemented in the **Security** module, the best way to validate it is to apply the rule from the [Model Editor](xref:112582).

> [!IMPORTANT]
> Make sure that the **Security** module is added to the list of required modules.

* Right-click the **Validation** | **Rules** node. Select **Add…** | **RuleRegularExpression**. Set the new rule's **ID** property to "Password is complex". Set **TargetType** to "DevExpress.ExpressApp.Security.ChangePasswordOnLogonParameters", **TargetPropertyName** to "NewPassword", **TargetContextIDs** to "ChangePassword" and **SkipNullOrEmptyValues** to "False". Set the **Pattern** property to "`^(?=.*[a-zA-Z])(?=.*\d).{6,}$`". Only passwords consisting of 6 or more characters and digits match this regular expression. Replace the **MessageTemplateMustMatchThe Pattern** value with a user-friendly message that describes password requirements. For instance, you can type "New password must consist of at least 6 alphanumeric characters."
	
	![Validation_NonPersistent_ME2](~/images/validation_nonpersistent_me2116614.png)
	
	> [!NOTE]
	> You can compose your own pattern to fit your password requirements. If you are not familiar with regular expressions, you can refer to the [regular expressions 101](https://regex101.com/library) website to search for an appropriate regular expression. If you want to prohibit the use of an empty password, create the **RuleRequiredField** rule instead of **RuleRegularExpression**.
* The **Change Password** dialog contains the **OK** button. This button is an [Action](xref:112622) that has the **DialogOK** ID. Navigate to **ActionDesign** | **Actions** | **DialogOK** and set the **ValidationContexts** property to "ChangePassword". As a result, the "ChangePassword" validation context identifier will be associated with the **DialogOK** Action.

* The Validation system is not fully initialized until a user has logged into the application. To initialize the Validation system, edit the [!include[File_Module](~/templates/file_module11171.md)] file, override the [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method, and handle the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event. In the event handler, access the Validation Module and call its [ValidationModule.InitializeRuleSet](xref:DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet) method. This will ensure that your validation rules are checked into the "Change Password on First Logon" screen.

    > [!NOTE]
    >
    > In v23.1 and higher, you can skip this step for .NET Core-based applications (both Blazor and WinForms). All required initialization is done automatically.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Validation;
//...
public override void Setup(XafApplication application) {
    base.Setup(application);
    application.SetupComplete += application_SetupComplete;
}
void application_SetupComplete(object sender, EventArgs e) {
    ValidationModule module = ((XafApplication)sender).Modules.FindModule<ValidationModule>();
    if (module != null) module.InitializeRuleSet();
}
```
***

Application administrators can still assign a weak password to a user (the **ResetPassword** Action). Use the solution above to validate the **ResetPasswordParameters.Password** property.

The following window appears when an end user enters a new password that does not meet the complexity requirements.

![Validation_NonPersistent_Password](~/images/validation_nonpersistent_password116615.png)
