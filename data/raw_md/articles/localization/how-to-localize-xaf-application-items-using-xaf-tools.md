---
uid: "119411"
seealso: []
title: 'How to: Localize XAF Application Items Using XAF Tools'
owner: Ekaterina Kiseleva
---
# How to: Localize XAF Application Items Using XAF Tools

This topic describes how to localize typical XAF application items using XAF tools. We recommend reviewing the [Application Model Basics](xref:112580) and [Localization Basics](xref:112595) topics before proceeding.


Refer to the [How to: Localize an XAF Application](xref:402956) topic for information on how to translate XAF applications.

You can localize parts of an XAF application in two ways:

* Using the [Localization Tool](xref:113297), which can be invoked from the **Model Editor Toolbar**. This tool gathers all the localizable values in one grid, provides the import/export functionality, as well as the ability to use the **Microsoft Translator** service.
* Directly in the [Model Editor](xref:112582) by translating each localizable value.

We recommend using the **Localization Tool** to speed up the localization process.

## Use the Localization Tool
Start the translation in the platform-agnostic module (_MySolution.Module_) and then proceed to the platform-specific modules. Follow the steps below to localize each XAF application module with the Localization Tool.

1. Click the **Localization** button in the [Model Editor Toolbar](xref:113327) to invoke the **XAF Localization** window.

	![|DevExpress XAF Model Editor: Localization](~/images/model_editor_toolbar_localization.png)
	
	![LocalizationTool](~/images/localizationtool116714.png)
	
	This window provides the grid editor with all localizable property names, paths, descriptions, and values. A toolbar with the base localization commands is also provided. The [Localization Tool](xref:113297) topic describes grid columns and this window's available actions.
2. In the **Localization** window toolbar, select the target language in the **Translation Language** drop-down list.
	
	![LocalizationToolTranslationLanguage](~/images/localizationtooltranslationlanguage116715.png)
	
	> [!NOTE]
	> The text supplied with the standard XAF modules are translated if you have successfully installed satellite assemblies for the target language.
3. Apply the **Untranslated non-calculated** filter using the **Filters** action.
	
	![LocalizationToolFilter](~/images/localizationtoolfilter116716.png)
	
	This filter selects the properties that have non-empty default language values with **Is Translated** and **Is Calculated** unchecked.
4. Translate all the values in the **Translated Value** column. Move focus to the next row pressing the ENTER key. If there are several properties with the same Default Language value, the **Multiple Values Translation** dialog is invoked. If you click **Yes**, the tool translates all these values at once and focuses the next value to be translated.
	
	![LocalizationToolCopying](~/images/localizationtoolcopying116717.png)
	
	> [!NOTE]
	> * You can use the **Translate…** button to automate the translation. Select one, several or all rows, and click **Translate…** or press CTRL+T. In the invoked dialog, select the original language (English by default), click **Translate** and the Microsoft Translator service translates it. An Internet connection is required for this feature, and automatic translation requires reviewing the results.
	> * If you are not fluent in the target language, you can hire a professional translator. Export the selected rows to a CSV file using the **Export** | **Selected records** command, and pass this file to the translator. The translator will edit the values in the Translated Value column using a spreadsheet or a plain text editor of their choice. The **Description** column content helps them see the context. The translated values can be loaded from a CSV file using the **Import** Action. The file encoding should be UTF-8 if the CSV file contains non-Latin characters.
5. When you have finished the translation, click Save or press CTRL+S to save changes to the Application Model. The translated properties are hidden due to the **Untranslated…** filter, and the **Is Translated** checkbox is checked after saving.
	
	![LocalizationToolSave](~/images/localizationtoolsave116718.png)
6. Next, apply the **Calculated** filter to review the calculated values.
	
	![LocalizationToolCalculatedFilter](~/images/localizationtoolcalculatedfilter116719.png)
7. After closing the **Localization** window, you can see the localized values in the Model Editor. Save the changes in the Model Editor.

A typical XAF application has platform-specific authentication, security strategy and module versions. For example, Windows Forms applications can have the **SchedulerWindowsFormsModule** module. This module extends the Application Model with localizable properties that are not available at the module level. You can have platform-specific Controllers that provide strings that need to be localized (action captions, tooltips, exceptions, and so on.).

## Localize an XAF Application Directly in the Model Editor
Follow the steps below to localize the main parts of your XAF application directly in the Model Editor. Note that some translation values contain properties' names (**ObjectCaptionFormat**, **DisplayFormat**, etc.) and should not be localized. 

1. Select the target language in the [Model Editor Toolbar](xref:113327).
2. Set the localized values to the **Application** root node's properties.
3. Expand the **ActionDesign** | **Actions** node. Set the localized values to all its child nodes' **Caption** properties. The **ShortCaption** and the **Tooltip** properties are localized automatically, as they expose **Caption** properties' values by default. Localize the **ConfirmationMessage** properties if required.
	> [!NOTE]
	> If you do not use the **Active Directory** authentication, the **Log On** window (web page) UI elements localization requires particular attention. The **Log On** and **Cancel** buttons are [Actions](xref:112622). These Actions have **Logon** and **DialogCancel** IDs and are localizable in the **ActionDesign** | **Actions** node.
4. Expand the **ActionDesign** | **DisableReasons** node and set localized values to its child nodes' **Caption** properties.
5. Expand the **BOModel** node and assign localized values to its child nodes' **Caption** properties. You can skip nodes of classes that are not represented in the application UI (for example, the **XPBaseObject** node). Note that localizing **ObjectCaptionFormat** properties may also be required. The **Caption** properties of **CreatableItems**, [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] and **Views** child nodes are automatically localized as they expose values from class captions by default.
6. Expand the **Localization** node and set localized values to its child nodes' **Value** properties. The **Exceptions** | **UserVisibleExceptions** child node localization requires particular attention. You can skip the **Exceptions** | **SystemExceptions** node, as it contains exceptions addressed to developers and administrators, and is invisible to end-users in normal application operation.
7. Expand the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] and localize the **Default** node caption.
8. If you use the **ValidationModule** module, expand the **Validation** node and assign localized values to the child node properties the globe glyph (![GlobeGlyph](~/images/globeglyph116550.png)) denotes.
	
	![Caption_Localized](~/images/caption_localized115378.png)
10. If you do not use the **Active Directory** authentication type, the **Log On** window (web page) localization requires particular attention. The **AuthenticationStandardLogonParameters** Detail View represents this window (web page) content, so navigate to the **Views** | **AuthenticationStandardLogonParameters_DetailView** node and set the localized value to its **Caption** property. Expand the **Items** child node and localize the **LogonText** node's **Text** property. Localize the **UserName** and **Passwords** node captions.
	> [!NOTE]
	> Do this for each separate platform-specific project. Use the [Model Editor](xref:112582) in each application project to localize UI elements on the **Log On** window (web page). See step 5 for instruction on how to localize **Log On** and **Cancel** Action captions. To access the message for failed login attempts, use the the **Localization** | **Exceptions** | **UserVisibleExceptions** | **Security** node.
	> * In an ASP.NET Core Blazor application, modify either **AuthenticationStandardLogonParameters_Blazor_DetailView** or **NoPasswordLogonParameters_DetailView** (depending on whether the password authentication is enabled).
	> * In a Windows Forms application, modify either **AuthenticationStandardLogonParameters_Win_DetailView** or **NoPasswordLogonParameters_Win_DetailView** (depending on whether the password authentication is enabled).

11. Invoke the [Model Editor](xref:112582) for the application project (Windows Forms) to see additional platform-specific **Localization** child nodes. For instance, in the Windows Forms application Model, you should assign localized values to **Confirmations**, **DialogButtons** and **FrameTemplates** child nodes.

> [!NOTE]
> If you received the **FormatException** or **MemberNotFoundException**, ensure that you have not localized a property name in a localizable value.

Refer to the following topics to learn how to localize particular messages in an application:

* [How to: Localize Custom String Constants](xref:112655)
* [How to: Localize a WinForms Template](xref:114495)
* [Localize Validation Messages](xref:113129)

The [Localize Standard XAF Modules and DevExpress Controls Used in an Application](xref:113301) topic describes how to localize built-in XAF Modules and DevExpress controls.
