---
uid: "113310"
seealso:
- linkId: DevExpress.ExpressApp.Utils.ITranslatorProvider
- linkId: "113297"
title: 'How to: Create a Custom Translation Provider for the Localization Tool'
---
# How to: Create a Custom Translation Provider for the Localization Tool

The [Localization Tool](xref:113297) utilizes the [Microsoft Translator](https://www.microsoft.com/en-us/translator/) as the translation provider. However, one of the notable features of our localization tool is the capability to use custom translation services. That means that you can use alternative translators. In this example, custom translation provider implementation is demonstrated.

To create a custom translation provider, you need  to create and register a class, implementing the [](xref:DevExpress.ExpressApp.Utils.ITranslatorProvider) interface. As an alternative to implementing it from scratch, you can create a descendant of the **TranslatorProviderBase** class, which already encompasses a good deal of functionality. This class also collects localized values in blocks to shorten the translation based on the online translation services. In this example, we will utilize the second approach.

The TranslatorProviderBase class descendant should implement some methods and properties of the ITranslatorProvider interface, which are not implemented by the base class.

* [ITranslatorProvider.Caption](xref:DevExpress.ExpressApp.Utils.ITranslatorProvider.Caption)
* [ITranslatorProvider.Description](xref:DevExpress.ExpressApp.Utils.ITranslatorProvider.Description)
* [ITranslatorProvider.GetLanguages](xref:DevExpress.ExpressApp.Utils.ITranslatorProvider.GetLanguages)

Additionally, overriding the [ITranslatorProvider.Translate](xref:DevExpress.ExpressApp.Utils.ITranslatorProvider.Translate(System.String[],System.String,System.String)) method is required.

Perform the following steps to implement the translation provider.

* Add the following class into the [platform-agnostic module project](xref:118045) (_MySolution.Module_), or add a new module to your solution and implement this class in it.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Utils;
	// ...
	public class MyTranslatorProvider : TranslatorProviderBase {
	    public MyTranslatorProvider() : base("<br />", 5000) { }
	
	    #region ITranslatorProvider Members
	    public override string Caption {
	        get { return "My Translate Provider"; }
	    }
	    public override string Description {
	        get { return "My Description"; }
	    }
	    public override string[] GetLanguages() {
	        string[] supportedLanguages = {"en", "fr", "de"};
	        return supportedLanguages;
	    }
	    public override string Translate(string text, string sourceLanguageCode,
	        string desinationLanguageCode) {
	        string result = "";
	        // Place the code that translates 'text' from 'sourceLanguageCode' to 'desinationLanguageCode' here
	        return result;
	    }
	    #endregion
	}
	```
	***
	
	Pass the maximum block length and separator to the base class constructor.
	
	> [!NOTE]
	> You can also override the auxiliary **CalculateSentences** method if you need to split the localized value into several parts to be localized separately. For instance, this is required when the translator service incorrectly handles special symbols, and also when you need to exclude strings enclosed in quotes and other special symbols. The **TranslatorProviderBase** class collects localized values, and splits them into small parts based on the **CalculateSentences** method, and then composes blocks from these smaller parts and processes them with the **Translate** method.
	
	> [!TIP]
	> To see a complete example, refer to the sources of the built-in **BingTranslatorProvider** available at _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Win\Core\ModelEditor\Localization\TranslatorProviders.cs_
* Modify the module's constructor to register a custom translation provider class.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public sealed partial class MySolutionModule : ModuleBase {
	    public MySolutionModule() {
	        InitializeComponent();
	        TranslatorProvider.RegisterProvider(new MyTranslatorProvider());
	    }
	}
	```
	***
* Rebuild your solution, and this custom translation provider will replace the default provider used by the **Localization Tool** in Visual Studio and at runtime.
