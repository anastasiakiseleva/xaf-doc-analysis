---
uid: "113297"
seealso:
- linkId: "112595"
title: Localization Tool
---
# Localization Tool

The Localization Tool is intended to simplify [localizing](xref:112595) XAF applications. While you can perform localization directly in the [Model Editor](xref:112582), in most cases the Localization Tool is more convenient. This topic provides general information for using this tool. Step-by-step instructions for using the Localization Tool are available in the [How to: Localize an XAF Application](xref:402956) topic.

> [!NOTE]
> Check to see if the ready-to-use [localizations of standard XAF modules and DevExpress controls](xref:113301) are available for your language before using the Localization Tool. You can significantly decrease the number of strings to be translated.

## Invoking the Localization Tool
The Localization Tool can be accessed via the **Localization** button on the [XAF Model Editor Toolbar](xref:113327). The tool is primarily intended to be used at design time. However, it is also available at runtime so users and application administrators can access its features.

![|DevExpress XAF Model Editor: Localization](~/images/model_editor_toolbar_localization.png)

![LocalizationTool](~/images/localizationtool116714.png)

The Localization button is inactive when there are no translation languages added. You should add one or more languages, as described in the [Localization Basics](xref:112595) topic, in order to use the Localization tool.

## Localization Window Elements
### Grid

The Localization window provides a grid editor, containing the following columns.

| Column&nbsp;Caption | Is&nbsp;Editable | Description |
|---|---|---|
| **Property&nbsp;Name** | No | The localizable property name. |
| **Default&nbsp;Language&nbsp;Value** | Yes | The property value in the default language. |
| **Translated&nbsp;Value** | Yes | The property value in the current translation language. |
| **Is&nbsp;Calculated** | No | A boolean value indicating whether or not the current property value is calculated based on another value. Typically, the calculated values should not be translated. |
| **Is&nbsp;Translated** | No | A boolean value indicating whether or not the current property value has a translated value in the current language. This column updates after saving changes. |
| **Is&nbsp;Modified** | No | A boolean value indicating whether or not the translated value was modified. This column updates after saving changes. |
| **Node&nbsp;Path** | No | The full path to the current property's node. Composed from node IDs, separated by backslashes. |
| **Description** | No | A current property description, that is also visible in the Model Editor in a yellow box below the property grid. |

You can use common [XtraGrid](https://www.devexpress.com/Products/NET/Controls/WinForms/Grid/index.xml?tab=features) features - search and sort values, reorder, hide and show columns, apply grouping and filters.

![LocalizationTool_GridFeatures](~/images/localizationtool_gridfeatures116799.png)

The **Default Language Value** and **Translated Value** columns are editable inline. You can select multiple rows, when required. The CTRL+A shortcut selects all rows that are visible due to current filtering.

### Toolbar

The localization window has the toolbar.

![LocalizationToolToolbar](~/images/localizationtooltoolbar116728.png)

The commands available on the toolbar are described in the table below.

| Command&nbsp;Caption | Shortcut | Description |
|---|---|---|
| ![Action_LocalizationSave](~/images/action_localizationsave124387.png)&nbsp;**Save** | CTRL+S | Saves the changes. |
| ![Action_LocalizationImport](~/images/action_localizationimport116725.png)&nbsp;**Import…** | CTRL+I | Imports the translation from the CSV file. |
| ![Action_LocalizationExport](~/images/action_localizationexport116726.png)&nbsp;**Export…** | CTRL+E | Performs export to the CSV file. Exposes two choice items - **Selected records** and **Modified records**. The **Is Translated** and **Is Calculated** columns are excluded when exporting. |
| **Translation&nbsp;Language** | &nbsp; | Provides a dropdown containing language aspects that are currently available in the Application Model. Use this command to choose the target translation language. To add a language, use the Language Manager dialog available in the Model Editor. Refer to the [Localization Basics](xref:112595) topic for details. |
| ![Action_Translate](~/images/action_translate116723.png)&nbsp;**Translate…** | CTRL+T | Performs the automatic translation of selected values via the **Microsoft Translator** online service. An Internet connection is required to execute this command. |
| ![Action_Filter](~/images/action_filter116724.png)&nbsp;**Filters** | &nbsp; | Provides a dropdown with predefined filters. Choose the required filter or select **Custom** to specify a custom one with the **Filter Editor**. |

The **Export…**, **Import…** and **Translate…** commands are also available in the grid context menus.

![LocalizationToolContextMenus](~/images/localizationtoolcontextmenus116729.png)

## Filtering
The localizable properties in the grid can be filtered to suit the current demands. You can use the XtraGrid [filtering capabilities](https://www.devexpress.com/products/net/controls/winforms/grid/), but its more convenient to use the **Filter** dropdown.

![LocalizationToolFilter](~/images/localizationtoolfilter116716.png)

The following predefined filters are supplied.

| Filter Name | Description |
|---|---|
| **None** | No filtering is applied. Choose this item to get the full list of localizable properties. |
| **Untranslated non-calculated** | Selects the properties that have non-empty default language values with **Is Translated** and **Is Calculated** unchecked. Choose this item to see the list of properties to be translated. Typically, the localization process should be started |
| **Untranslated calculated** | Selects the properties that have non-empty default language values with **Is Translated** unchecked and **Is Calculated** checked. Choose this item to check if there are calculated properties to be translated. |
| **Untranslated** | Selects the properties that have non-empty default language values with **Is Translated** unchecked. |
| **Translated** | Selects the properties that have non-empty default language values with **Is Translated** checked. |
| **Non-calculated** | Selects the properties that have non-empty default language values with **Is Calculated** unchecked. |
| **Calculated** | Selects the properties that have non-empty default language values with **Is Calculated** checked. |
| **Custom** | Invokes the [Filter Editor](xref:7788) dialog. Choose this item to specify a custom filter. |

You can use the custom filter to exclude certain nodes from your "to be translated list". For instance, you can skip the **SystemExceptions** node, as it contains exceptions addressed to developers and administrators, and invisible to end-users in normal application operation. The following image illustrates the corresponding customized filter based on the predefined **Untranslated non-calculated** filter.

![LocalizationToolCustomFilter](~/images/localizationtoolcustomfilter116730.png)

## Editing Values
The **Default Language Value** and **Translated Value** columns are editable inline. So, you can easily perform manual translation cell by cell, just like in a spreadsheet editor. Additionally, you can perform modifications of default language values when required. Values that do not fit the cell width are displayed multiline.

![LocalizationToolMultiline](~/images/localizationtoolmultiline116732.png)

If you edit a value and press ENTER, the value below is focused automatically. If the translated value occurs several times, the following dialog is invoked.

![LocalizationToolCopying](~/images/localizationtoolcopying116717.png)

If you choose **Yes**, all the similar values will be automatically replaced with your translation. You can check "Use always" to remember your choice and suppress this dialog until the next use of the **Localization** tool. The **Save** action passes changes to the Model Editor. Note that the **Is Translated** state is not updated immediately after translating a value. It changes only after executing the **Save** action. This behavior is implemented to avoid hiding the just translated value by the **Translated** filter.

The modified records are displayed in bold, as in the Model Editor's property grid.

## Microsoft® Translator Service Support
The **Translate…** command is designed to perform an automatic translation of the selected values via the Microsoft® Translator service. This is a free online translation service provided by Microsoft. You can access its web front-end at [https://www.bing.com/search?q=Bing+translate](https://www.bing.com/search?q=Bing+translate). The **Translate…** action allows you to get the benefit of this service without leaving the **Localization** window. This action invokes the following dialog.

![LocalizationToolMsTranslate](~/images/localizationtoolmstranslate116733.png)

If the default language is not English, you can select one of the supported source languages. Then click **Translate**, and the selected default language values will be passed to the Microsoft Translator service. The translated values are modified with the results from the service. If the translation is time-consuming, the progress bar will be displayed. Of course, an active Internet connection is required. However, the automatic translation is not perfect and typically requires manual review.

> [!NOTE]
> If you run the Localization Tool from the standalone Model Editor, and you are connecting to the Internet through a proxy server, it is recommended that you add the following setting to the Model Editor's configuration file.
> ```XML
<configuration>
    <system.net>
        <settings>
            <servicePointManager expect100Continue="false" />
  ...
```
> This file is located in the same folder as the Model Editor executable (_[!include[PathToXafTools](~/templates/path-to-xaf-tools.md)]\Model Editor\DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe_).

The Microsoft® Translator limits the amount of text you can translate in a given time period. If you need to translate a large number of strings, consider implementing a custom translation provider as described in the following article: [How to: Create a Custom Translation Provider for the Localization Tool](xref:113310). Your custom translation provider can use an alternative translation method, such as [Google Translate](https://translate.google.com/) or a local dictionary.

## Import/Export Functionality
The **Export…** command provides you with the ability to export selected, modified or all records to a CSV file.

![LocalizationExportAction](~/images/localizationexportaction116798.png)

The **Is Translated** and **Is Calculated** columns are omitted when exporting. The comma character is used as a separator. The output file encoding is UTF-8. Below is a sample of the output file (descriptions are skipped to save space).

``"Property Name","en","de","Node Path","Description"``

``"Title","MainDemo - Outlook in 60 minutes!","MainDemo - Outlook in 60 Minuten!","Application","..."``

``"Subtitle","XAF demo application","XAF Demo-Anwendung","Application","..."``

``"Caption","Refresh","Aktualisieren","ActionDesign\Actions\Refresh","..."``

``"Caption","Save","Speichern","ActionDesign\Actions\Save","..."``

You can pass the CSV file to a professional translator and ask them to edit the values in the Translated Value column using a spreadsheet or plaintext editor of their choice. The **Description** column text helps to see the context in this instance.

The **Import…** command provides you with the ability to import translations from the CSV file. This command replaces the default and translated values with values found in the specified CSV file. Rows with an invalid node path or property name are skipped. The CSV file encoding should be UTF-8. If the translator saved the CSV file in another encoding, you should convert it to UTF-8 before importing.

## Typical Use Cases
* ### The developer performs the localization
	
	If you are fluent in the target language, you can translate the localizable values, either manually or with the help of the Microsoft Translator service.
* ### The developer creates a CSV file for professional translator
	
	If you have hired a professional translator, you can use the **Export…** |  **Selected records** command to create a CSV file containing currently selected rows for him. The translated values can be loaded back via the **Import** command.
* ### The localization of standard XAF modules and DevExpress controls is reused
	
	The common set of localizable values can be translated once, exported to the CSV files and reused in each new application. This approach can be used if there are no [ready-to-use language resources](xref:113301) for the target language. Use the **Export…** | **Modified records** command to export modified records only.

## Settings Storage
The Localization Tool saves its settings between runs (grid settings, translation language and so on) in the system registry under the _HKEY_CURRENT_USER\Software\Developer Express\XAF\Model Editor\Localization_ key. You can delete this key to reset settings.
