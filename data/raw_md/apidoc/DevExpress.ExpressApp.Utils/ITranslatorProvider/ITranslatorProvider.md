---
uid: DevExpress.ExpressApp.Utils.ITranslatorProvider
name: ITranslatorProvider
type: Interface
summary: Declares members implemented by classes representing translation providers, which can be used in the [Localization Tool](xref:113297).
syntax:
  content: public interface ITranslatorProvider
seealso:
- linkId: DevExpress.ExpressApp.Utils.ITranslatorProvider._members
  altText: ITranslatorProvider Members
---
In order to create a custom translator you should create a custom translation provider class, implementing the **ITranslatorProvider** interface. To register a custom translation provider class, add the following code to the module's constructor:

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        InitializeComponent();
        TranslatorProvider.RegisterProvider(new MyTranslationProvider());
    }
}
```
***

In this snippet, the **MyTranslationProvider** is the class implementing **ITranslatorProvider** interface.

As an alternative to implementing the **ITranslatorProvider**  interface from scratch, you can create a descendant of the **TranslationProviderBase** class, which already encompasses a good deal of functionality. This class also collects localized values in blocks, to shorten the translation, based on the online translation services. You should specify the size of the block, as well as the separator symbol in the constructor of the **TranslatorProviderBase** class. The example of implementing such a descendant is provided in the [How to: Create a Custom Translation Provider for the Localization Tool](xref:113310) topic.