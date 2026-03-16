---
uid: "113130"
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport
- linkId: "400004"
owner: Ekaterina Kiseleva
title: 'Apply HTML Formatting to WinForms View Items'
---
# Apply HTML Formatting to WinForms View Items

This article describes how to use HTML formatting in WinForms XAF applications.

The following XAF UI elements support HTML formatting:

* The Static Text [View Item](xref:112612)'s text.
* The Property Editor's captions in [Detail Views](xref:112611#detail-view).
* Column captions in WinForms applications ([](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor)). 
	
Refer to [HTML Text Formatting](xref:4874) for a list of supported HTML tags.


## Getting Started

You should open the [Application Model](xref:112580)'s **Options** node and set the [IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting) property to **true** before you can use HTML formatting.

You can access this property from the WinForms module or application project's [Model Editor](xref:112582).

![Enable_HTML_Formatting](~/images/EnableHtmlFormatting.png)

The instructions below demonstrate how to apply HTML formatting to various UI elements in your application. The examples in this article use the Main Demo (_[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_).

## Static Text View Item's Text

This section describes how to access the Static Text [View Item](xref:112612)'s text and change its appearance with HTML tags.

Set the **Text** property of the [Application Model](xref:112580)'s **Views** | **AuthenticationStandardLogonParameters_DetailView_Demo** | **Items** | **LogonText** node  to \<color=green>Welcome! Please enter your user name and password below.\</color>.

The following image shows the resulting login window:

![HTML_Formatting1](~/images/html_formatting1116154.png)

## Property Editor's Caption

This section describes how to access a Property Editor's caption and change its appearance with HTML tags.

Set the **Caption** property of the Application Model's **Views** | **Contact_DetailView** | **Items** | **WebPageAddress** node to `<size=12><color=red><b>Web </b><color=0,255,0><i>Page </i><color=#0000FF><u>Address</u></color></size>`.

The following image shows a part of the resulting Contact [Detail View](xref:112611#detail-view):

![HTML_Formatting2](~/images/html_formatting2116155.png)

## Column's Caption of the Default List Editor

This section describes how to access a column's caption inside the default [List Editor](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and change this captions's appearance with HTML tags.

Set the **Caption** property of the Application Model's **Views** | **Contact_ListView** | **Columns** | **LastName** node to `<size=10><color=#CFCAFF><size=+4>L<color=#B0A8FF><size=+4>A<color=#6F79FF><size=+4>S<color=#4D3EFF><size=+4>T <color=#4D3EFF><size=-4>N<color=#6F79FF><size=-4>A<color=#B0A8FF><size=-4>M<color=#CFCAFF><size=-4>E</color></size>`. 

The following image shows the resulting Contact [List View](xref:112611#list-view):

![HTML_Formatting3](~/images/html_formatting3116156.png)
