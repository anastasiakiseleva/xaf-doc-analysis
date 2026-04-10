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

![Change password dialog](~/images/change-password-dialog.png)

The `NewPassword` is a property to be validated. As this property is implemented in the **Security** module, the best way to validate it is to apply the rule from the [Model Editor](xref:112582).

> [!IMPORTANT]
> Make sure that the **Security** module is added to the list of required modules.

1. In the Model Editor, right-click the **Validation** | **Rules** node. Select **Add…** | **RuleRegularExpression**. Specify the following rule's settings:

    * `ID` = `Password is complex`
    * `TargetType` = `DevExpress.ExpressApp.Security.ChangePasswordOnLogonParameters`
    * `TargetPropertyName` = `NewPassword`
    * `TargetContextIDs` = `ChangePassword`
    * `SkipNullOrEmptyValues` = `False` 
    * `Pattern` = `^(?=.*[a-zA-Z])(?=.*\d).{6,}$`
    * `MessageTemplateMustMatchPattern` = `New password must consist of at least 6 alphanumeric characters.`
	
	![Model Editor - Validation Properties](~/images/model-editor-validation-complex-password.png)
	
    You can compose your own pattern to fit your password requirements. If you are not familiar with regular expressions, you can refer to the [regular expressions 101](https://regex101.com/library) website to search for an appropriate regular expression. If you want to prohibit the use of an empty password, create the **RuleRequiredField** rule instead of **RuleRegularExpression**.

1. The **Change Password** dialog contains the **OK** button. This button is an [Action](xref:112622) that has the **DialogOK** ID. Navigate to **ActionDesign** | **Actions** | **DialogOK** and set the `ValidationContexts` property to `ChangePassword`. As a result, the `ChangePassword` validation context identifier will be associated with the **DialogOK** Action.

Application administrators can still assign a weak password to a user (the **ResetPassword** Action). Use the solution above to validate the `ResetPasswordParameters.Password` property.

When an end user enters a new password that does not meet the complexity requirements, the error message appears.

![Validation Error Message](~/images/validation-error-toast-notification.png)
