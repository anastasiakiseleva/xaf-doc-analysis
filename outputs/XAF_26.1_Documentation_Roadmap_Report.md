# XAF 26.1 Documentation Roadmap Report
**Generated:** 2026-02-13 10:29
**Analysis Date:** February 13, 2026

**Note:** This report excludes 31 tickets already marked as 'DocIssueFixed'.
Only analyzing unfixed documentation issues requiring action.

---

## Executive Summary

- **Total Documentation Issues:** 26
- **Roadmap-Aligned Issues:** 25 (96%)
- **Features Affected:** 12 / 18
- **Unique Documentation URLs:** 109

### Priority Distribution

| Priority | Issues | Unresolved | Estimated Effort |
|----------|--------|------------|------------------|
| P0 Critical Pre Release | 12 | 10 | 20h |
| P1 High Pre Release | 35 | 27 | 54h |
| P2 Medium Post Release | 37 | 31 | 62h |
| P3 Low Post Release | 2 | 2 | 4h |
| P4 Proactive New Features | 0 | 0 | 0h |

---


## P0 CRITICAL PRE RELEASE

**⚠️ MUST FIX BEFORE 26.1 RELEASE**
These features have breaking changes or new requirements that will cause immediate customer confusion if documentation is not updated.

---

### [Blazor] CSP - Remove style-src: unsafe-inline requirement

**Issues:** 2 (2 unresolved)  
**Affected Documentation:** 2 URL(s)  
**Estimated Effort:** 4 hours

#### 📄 Affected Documentation Topics

- [Content Security Policy#Why Unsafe Inline Style Source Is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)
- [Active Directory And Oauth2 Authentication Providers In Winforms Applications](https://docs.devexpress.com/eXpressAppFramework/404752/data-security-and-safety/security-system/authentication/oauth-and-custom-authentication/active-directory-and-oauth2-authentication-providers-in-winforms-applications)

#### 🎫 Documentation Issues

##### 📦 T1313595: Describe why  "unsafe-inline" in CSP is required in XAF Blazor Apps

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The customer is inquiring about the necessity of using the "unsafe-inline" attribute in the Content Security Policy (CSP) for XAF Blazor Apps. It has been clarified that it is not possible to avoid using this attribute. A solution outlining the reasons for this requirement has been suggested, indica...

**Issue:** The customer doesn't understand whether it is possible to avoid using this attribute (not possible)

**Proposed Solution:** Write a section similar to this one:
[Why unsafe-inline Style Source is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)

Contact <PERSON> R for any questions

---

##### 📦 T1285906: OAuth and Custom Authentication - a crucial aspect is not emphasized

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue highlights a missing detail in the documentation regarding the `NameClaimType` value in OAuth and Custom Authentication for applications using `DevExpress.ExpressApp.Security.UserManager`. It is critical for the `ClaimsIdentity.Name` value to be present when parsing a principal from a thir...

**Issue:** Help topics of this help section miss the crucial piece of information - the necessity to set the `NameClaimType` value. The reason for this is that our `DevExpress.ExpressApp.Security.UserManager` class expects the [ClaimsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsidentity.name?view=net-9.0#remarks) value to exist (e.g., to be not null) when parsing a...

**Proposed Solution:** Reflect this information in our documentation and emphasize its importance.

---


### [Blazor] Simplified Blazor project format with no Startup.cs

**Issues:** 10 (8 unresolved)  
**Affected Documentation:** 10 URL(s)  
**Estimated Effort:** 16 hours

#### 📄 Affected Documentation Topics

- [Content Security Policy#Why Unsafe Inline Style Source Is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [Custom Easy Test Commands](https://docs.devexpress.com/eXpressAppFramework/113340/debugging-testing-and-error-handling/functional-tests-easy-test/write-tests-human-readable/custom-easy-test-commands)
- [Localize An Xaf Application#Single Language Support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [How To Choose Optimal Query Splitting Behavior](https://docs.devexpress.com/eXpressAppFramework/404862/business-model-design-orm/business-model-design-with-entity-framework-core/performance/how-to-choose-optimal-query-splitting-behavior)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)
- [Devexpress.Expressapp.Scheduler.Blazor.Scheduleroptions.Viewtypes?P=Net8](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1311731: Custom EasyTest Commands | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 610

**Summary:** The customer provided feedback regarding the lack of Blazor instructions on the DevExpress documentation page for custom EasyTest commands. They indicated that the page was not helpful and suggested the addition of sample code and information. The ticket includes links to related documentation for f...

---

##### 📦 T1313595: Describe why  "unsafe-inline" in CSP is required in XAF Blazor Apps

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The customer is inquiring about the necessity of using the "unsafe-inline" attribute in the Content Security Policy (CSP) for XAF Blazor Apps. It has been clarified that it is not possible to avoid using this attribute. A solution outlining the reasons for this requirement has been suggested, indica...

**Issue:** The customer doesn't understand whether it is possible to avoid using this attribute (not possible)

**Proposed Solution:** Write a section similar to this one:
[Why unsafe-inline Style Source is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)

Contact <PERSON> R for any questions

---

##### 📦 T1313180: The translation dialog appears in browser, as the language is changed several seconds after app loading

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue described involves a translation dialog appearing in the browser when a user opens an XAF app due to a delay in the language setting from "en" to "cs". This occurs as the browser initially receives `<html lang="en" />` content, which is later dynamically changed. The solution involves cus...

**Issue:** When user opens XAF app, browser receives `<html lang="en" />` content which is dynamically changed to lang="cs" in few seconds. In between browser shows the translation popup.

**Proposed Solution:** Add information to the [Single language support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support) section:

To resolve the issue, customize the `<html>` tag in the `Pages\_Host.cshtml` file In XAF Blazor application.  Specify the correct culture: `<html lang="cs" />` . After that, the correct culture should be set since the i...

---

##### 📦 T1303299: Scehduler configuration docs are difficult to find

**Status:** Archived  
**Gap Type:** Discoverability Gap  
**Customer References:** 1  
**Priority Score:** 430

**Summary:** The customer expressed dissatisfaction with the difficulty in locating code snippets for Scheduler configuration. The primary issue is not the absence of snippets but their accessibility and discoverability via search engines. A specific code snippet is found in the help topic regarding SchedulerOpt...

**Issue:** The customer is unhappy with the lack of code snippets regarding Scheduler configuration. However, the real issue lies in the fact that those code snippets are difficult to find.

We have a code snippet in the following help topic: [SchedulerOptions\.ViewTypes Property](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8).

Howev...

---

##### ✅ T1318737: How to: Choose the Optimal Query Splitting Behavior in Entity Framework Core | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 6  
**Priority Score:** 380

**Summary:** The ticket raises an issue regarding the documentation on optimal query splitting behavior in Entity Framework Core related to the `UseConnectionString()` method. The customer notes that while the approach to remove database-specific code on startup is beneficial, it also leads to concerns about its...

---



## P1 HIGH PRE RELEASE

**🔴 HIGH PRIORITY - PRE-RELEASE**
Major features with significant documentation needs. Strongly recommended before release.

---

### [Core] EF Core 10 Support

**Issues:** 11 (9 unresolved)  
**Affected Documentation:** 12 URL(s)  
**Estimated Effort:** 18 hours

#### 📄 Affected Documentation Topics

- [Drag And Drop Behavior](https://docs.devexpress.com/WindowsForms/118656/common-features/behaviors/drag-and-drop-behavior)
- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [Custom Easy Test Commands](https://docs.devexpress.com/eXpressAppFramework/113340/debugging-testing-and-error-handling/functional-tests-easy-test/write-tests-human-readable/custom-easy-test-commands)
- [Key Properties#Entity Framework Ef](https://docs.devexpress.com/eXpressAppFramework/113665/business-model-design-orm/data-types-supported-by-built-in-editors/key-properties#entity-framework-ef)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Active Directory And Oauth2 Authentication Providers In Winforms Applications](https://docs.devexpress.com/eXpressAppFramework/404752/data-security-and-safety/security-system/authentication/oauth-and-custom-authentication/active-directory-and-oauth2-authentication-providers-in-winforms-applications)
- [How To Choose Optimal Query Splitting Behavior](https://docs.devexpress.com/eXpressAppFramework/404862/business-model-design-orm/business-model-design-with-entity-framework-core/performance/how-to-choose-optimal-query-splitting-behavior)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1311731: Custom EasyTest Commands | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 610

**Summary:** The customer provided feedback regarding the lack of Blazor instructions on the DevExpress documentation page for custom EasyTest commands. They indicated that the page was not helpful and suggested the addition of sample code and information. The ticket includes links to related documentation for f...

---

##### 📦 T1285906: OAuth and Custom Authentication - a crucial aspect is not emphasized

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue highlights a missing detail in the documentation regarding the `NameClaimType` value in OAuth and Custom Authentication for applications using `DevExpress.ExpressApp.Security.UserManager`. It is critical for the `ClaimsIdentity.Name` value to be present when parsing a principal from a thir...

**Issue:** Help topics of this help section miss the crucial piece of information - the necessity to set the `NameClaimType` value. The reason for this is that our `DevExpress.ExpressApp.Security.UserManager` class expects the [ClaimsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsidentity.name?view=net-9.0#remarks) value to exist (e.g., to be not null) when parsing a...

**Proposed Solution:** Reflect this information in our documentation and emphasize its importance.

---

##### ✅ T1318737: How to: Choose the Optimal Query Splitting Behavior in Entity Framework Core | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 6  
**Priority Score:** 380

**Summary:** The ticket raises an issue regarding the documentation on optimal query splitting behavior in Entity Framework Core related to the `UseConnectionString()` method. The customer notes that while the approach to remove database-specific code on startup is beneficial, it also leads to concerns about its...

---

##### 📦 T1282060: Implement a Property Editor Based on a Custom Component 

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 310

**Summary:** The user is requesting assistance with implementing a property editor based on a custom component, as the referenced article does not provide guidance on using a custom component. The proposed solution is to include an example with a custom razor component.

**Issue:** the article 'Implement a Property Editor Based on a Custom Component' doesn't show how to use a custom component at all.

**Proposed Solution:** We need to add an example with a custom razor component

---

##### 🔴 T1320904: TreeList - Drag information is not recalculated when the Handled property is set to true

**Status:** Active  
**Gap Type:** Quality Gap  
**Customer References:** 2  
**Priority Score:** 290

**Summary:** The issue described involves the DragOver event not recalculating event arguments in the DragDropBehavior of TreeList when the Handled property is set to true. The solution is to call `e.Default` within the DragOver event to ensure that automatic calculation occurs properly in scenarios where Handle...

**Issue:** It is not described how to properly handle the DragOver event for DragDropBehavior. The issue is that with certain implementations, the user expects that automatic calculation of event arguments for DragOver occur the next time it triggers when **Handled** event argument is set to true.

**Proposed Solution:** Add a note or remark that it is necessary to call `e.Default` in the DragOver event to trigger calculation again in usage scenarios where user set the Handled event argument to true. In short, call `e.Default` first before overriding event arguments as automatic calculation does not happen until after DragOver.

---

##### 📦 T1283433: [S ] Key Properties - EF Core string key property

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 2  
**Priority Score:** 120

**Summary:** This ticket discusses the common issue of creating a custom string key property in Entity Framework Core and suggests enhancing the documentation to provide clarity on this process. It highlights specific error handling in XAF and references additional resources for further assistance.

**Issue:** The creation of a custom key property of the string type is a popular question that generates excessive support traffic. While the question itself is not entirely related to XAF, it would be beneficial to elaborate on this usage scenario in our documentation.

**Proposed Solution:** In the [Entity Framework \(EF\)](https://docs.devexpress.com/eXpressAppFramework/113665/business-model-design-orm/data-types-supported-by-built-in-editors/key-properties#entity-framework-ef) section, add a sub-section that describes the task of creating a custom string key property.

The task itself is described in the following Stack Overflow thread: [How to use String property as primary key in ...

---

##### 📦 T1279094: [S 3] A missing example of using CustomCreateObjectSpaceProvider 

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 110

**Summary:** The ticket discusses the lack of clarity regarding the definition and implementation of `CustomCreateObjectSpaceProvider` in DevExpress. It provides code examples to demonstrate the correct way to define a custom object space provider, ensuring the integration of specific data store configurations.

**Issue:** It is not clear how to define # CustomCreateObjectSpaceProvider

**Proposed Solution:** ```cs
public class CustomXPObjectSpaceProvider :XPObjectSpaceProvider {
    public CustomXPObjectSpaceProvider(IXpoDataStoreProvider dataStoreProvider, bool threadSafe) : base(dataStoreProvider, threadSafe) { }
    public CustomXPObjectSpaceProvider(string connectionString, IDbConnection connection, bool threadSafe) : base(connectionString, connection, threadSafe) { }
    protected override IObjec...

---


### [Blazor] Blazor Reports - Add and Customize ViewDataSource in Report Designer

**Issues:** 12 (11 unresolved)  
**Affected Documentation:** 17 URL(s)  
**Estimated Effort:** 22 hours

#### 📄 Affected Documentation Topics

- [Content Security Policy#Why Unsafe Inline Style Source Is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)
- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [Format A Business Object Caption?V=22.1](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [Custom Easy Test Commands](https://docs.devexpress.com/eXpressAppFramework/113340/debugging-testing-and-error-handling/functional-tests-easy-test/write-tests-human-readable/custom-easy-test-commands)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Localize An Xaf Application#Single Language Support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support)
- [Add New Net Core Xaf Module](https://docs.devexpress.com/eXpressAppFramework/403415/migration-to-net/add-new-net-core-xaf-module)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)
- [Devexpress.Expressapp.Model.Imodelclass.Objectcaptionformat](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Model.IModelClass.ObjectCaptionFormat)
- [Devexpress.Expressapp.Scheduler.Blazor.Scheduleroptions.Viewtypes?P=Net8](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8)
- [Devexpress.Persistent.Base.Objectcaptionformatattribute](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Persistent.Base.ObjectCaptionFormatAttribute)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1311731: Custom EasyTest Commands | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 610

**Summary:** The customer provided feedback regarding the lack of Blazor instructions on the DevExpress documentation page for custom EasyTest commands. They indicated that the page was not helpful and suggested the addition of sample code and information. The ticket includes links to related documentation for f...

---

##### 📦 T1313595: Describe why  "unsafe-inline" in CSP is required in XAF Blazor Apps

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The customer is inquiring about the necessity of using the "unsafe-inline" attribute in the Content Security Policy (CSP) for XAF Blazor Apps. It has been clarified that it is not possible to avoid using this attribute. A solution outlining the reasons for this requirement has been suggested, indica...

**Issue:** The customer doesn't understand whether it is possible to avoid using this attribute (not possible)

**Proposed Solution:** Write a section similar to this one:
[Why unsafe-inline Style Source is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)

Contact <PERSON> R for any questions

---

##### 📦 T1313180: The translation dialog appears in browser, as the language is changed several seconds after app loading

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue described involves a translation dialog appearing in the browser when a user opens an XAF app due to a delay in the language setting from "en" to "cs". This occurs as the browser initially receives `<html lang="en" />` content, which is later dynamically changed. The solution involves cus...

**Issue:** When user opens XAF app, browser receives `<html lang="en" />` content which is dynamically changed to lang="cs" in few seconds. In between browser shows the translation popup.

**Proposed Solution:** Add information to the [Single language support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support) section:

To resolve the issue, customize the `<html>` tag in the `Pages\_Host.cshtml` file In XAF Blazor application.  Specify the correct culture: `<html lang="cs" />` . After that, the correct culture should be set since the i...

---

##### 📦 T1303299: Scehduler configuration docs are difficult to find

**Status:** Archived  
**Gap Type:** Discoverability Gap  
**Customer References:** 1  
**Priority Score:** 430

**Summary:** The customer expressed dissatisfaction with the difficulty in locating code snippets for Scheduler configuration. The primary issue is not the absence of snippets but their accessibility and discoverability via search engines. A specific code snippet is found in the help topic regarding SchedulerOpt...

**Issue:** The customer is unhappy with the lack of code snippets regarding Scheduler configuration. However, the real issue lies in the fact that those code snippets are difficult to find.

We have a code snippet in the following help topic: [SchedulerOptions\.ViewTypes Property](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8).

Howev...

---

##### 📦 T1315692: ObjectCaptionFormatAttribute Class - old info was lost

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer reported that the information from an old help topic, "Format a Business Object Caption," was not transferred to the current documentation of the "ObjectCaptionFormatAttribute Class." The solution proposed is to add the relevant information, including screenshots and examples, from the ...

**Issue:** We had the following help topic, which is now discontinued: [Format a Business Object Caption](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1). Selecting a newer version redirects to [ObjectCaptionFormatAttribute Class](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Pers...

**Proposed Solution:** Add the information from the old help topic to the attribute's help topic.

---

##### 🔴 T1320766: Add a New .NET XAF Module to an XAF Application | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Active  
**Gap Type:** True Gap  
**Customer References:** 7  
**Priority Score:** 270

**Summary:** The customer reported that the wizard described in the DevExpress documentation for adding a new .NET XAF Module is obsolete. They indicated that when attempting to use it in Visual Studio, an error message is displayed, and they are forced to use a new wizard that does not support the addition of a...

---


### [Blazor] XAF AI Module

**Issues:** 12 (7 unresolved)  
**Affected Documentation:** 12 URL(s)  
**Estimated Effort:** 14 hours

#### 📄 Affected Documentation Topics

- [Drag And Drop Behavior](https://docs.devexpress.com/WindowsForms/118656/common-features/behaviors/drag-and-drop-behavior)
- [Xpo Extensions For Aspnet Core Di?Utm_Source=Supportcenter&Utm_Medium=Website&Utm_Campaign=Docs Feedback&Utm_Content=T1054062](https://docs.devexpress.com/XPO/403009/connect-to-a-data-store/xpo-extensions-for-aspnet-core-di?utm_source=SupportCenter&utm_medium=website&utm_campaign=docs-feedback&utm_content=T1054062)
- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Format A Property Value](https://docs.devexpress.com/eXpressAppFramework/402141/getting-started/in-depth-tutorial-blazor/customize-data-display-and-view-layout/format-a-property-value)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Active Directory And Oauth2 Authentication Providers In Winforms Applications](https://docs.devexpress.com/eXpressAppFramework/404752/data-security-and-safety/security-system/authentication/oauth-and-custom-authentication/active-directory-and-oauth2-authentication-providers-in-winforms-applications)
- [How To Choose Optimal Query Splitting Behavior](https://docs.devexpress.com/eXpressAppFramework/404862/business-model-design-orm/business-model-design-with-entity-framework-core/performance/how-to-choose-optimal-query-splitting-behavior)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1285906: OAuth and Custom Authentication - a crucial aspect is not emphasized

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue highlights a missing detail in the documentation regarding the `NameClaimType` value in OAuth and Custom Authentication for applications using `DevExpress.ExpressApp.Security.UserManager`. It is critical for the `ClaimsIdentity.Name` value to be present when parsing a principal from a thir...

**Issue:** Help topics of this help section miss the crucial piece of information - the necessity to set the `NameClaimType` value. The reason for this is that our `DevExpress.ExpressApp.Security.UserManager` class expects the [ClaimsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsidentity.name?view=net-9.0#remarks) value to exist (e.g., to be not null) when parsing a...

**Proposed Solution:** Reflect this information in our documentation and emphasize its importance.

---

##### ✅ T1318737: How to: Choose the Optimal Query Splitting Behavior in Entity Framework Core | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 6  
**Priority Score:** 380

**Summary:** The ticket raises an issue regarding the documentation on optimal query splitting behavior in Entity Framework Core related to the `UseConnectionString()` method. The customer notes that while the approach to remove database-specific code on startup is beneficial, it also leads to concerns about its...

---

##### ✅ T1309006: Format a Property Value | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 320

**Summary:** The customer encountered an issue with the documentation regarding the `DisplayFormat` property not being available in the 25.1 version of the product. They suggested improvements to the documentation, particularly related to formatting property values for the `DueDate` and `StartDate` nodes in thei...

---

##### 🔴 T1320904: TreeList - Drag information is not recalculated when the Handled property is set to true

**Status:** Active  
**Gap Type:** Quality Gap  
**Customer References:** 2  
**Priority Score:** 290

**Summary:** The issue described involves the DragOver event not recalculating event arguments in the DragDropBehavior of TreeList when the Handled property is set to true. The solution is to call `e.Default` within the DragOver event to ensure that automatic calculation occurs properly in scenarios where Handle...

**Issue:** It is not described how to properly handle the DragOver event for DragDropBehavior. The issue is that with certain implementations, the user expects that automatic calculation of event arguments for DragOver occur the next time it triggers when **Handled** event argument is set to true.

**Proposed Solution:** Add a note or remark that it is necessary to call `e.Default` in the DragOver event to trigger calculation again in usage scenarios where user set the Handled event argument to true. In short, call `e.Default` first before overriding event arguments as automatic calculation does not happen until after DragOver.

---

##### ✅ T1318183: XPO Extensions for ASP.NET Core Dependency Injection | XPO (.NET ORM Library) | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 12  
**Priority Score:** 250

**Summary:** This ticket contains feedback regarding the absence of a v25.2 version of the Xpo.Extensions for ASP.NET Core Dependency Injection. The customer's concern is about the documentation's lack of information on this version. They provided links to various documentation pages and also created a separate ...

---

##### ✅ T1306062: Create a Calculated Property - useless instruction

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 130

**Summary:** The customer has raised an issue regarding Step 3 of the documentation for creating a calculated property, highlighting that the instruction to run the application in debug mode with an attached debugger is unnecessary. The suggested solution is to simplify the instruction to just running the applic...

**Issue:** Step 3 contains the following instruction that contains useless specifics:

> Run the application in debug mode with attached debugger.

**Proposed Solution:** Change the instruction as follows:

> Run the application.

---

##### 📦 T1289742: Add documentation about how to use xUnit

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 120

**Summary:** The issue raised is about the lack of clear documentation on how to use xUnit for testing applications. The customer finds it difficult to understand what code needs to be written for tests. The proposed solution is to create examples of tests that demonstrate the use of various commands in action, ...

**Issue:** It is almost impossible to understand what code to write in tests to test an application.

**Proposed Solution:** Write several real examples of such tests that shows some of command in action. List all available commands in documentation.

---



## P2 MEDIUM POST RELEASE

**🟡 MEDIUM PRIORITY - POST-RELEASE OK**
Important improvements that can be addressed shortly after release.

---

### [Blazor] Blazor Model Editor

**Issues:** 11 (9 unresolved)  
**Affected Documentation:** 13 URL(s)  
**Estimated Effort:** 18 hours

#### 📄 Affected Documentation Topics

- [Content Security Policy#Why Unsafe Inline Style Source Is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [Localize An Xaf Application Net Framework](https://docs.devexpress.com/eXpressAppFramework/113250/localization/localize-an-xaf-application-net-framework)
- [Custom Easy Test Commands](https://docs.devexpress.com/eXpressAppFramework/113340/debugging-testing-and-error-handling/functional-tests-easy-test/write-tests-human-readable/custom-easy-test-commands)
- [How To Localize A Winforms Template](https://docs.devexpress.com/eXpressAppFramework/114495/localization/how-to-localize-a-winforms-template)
- [Format A Property Value](https://docs.devexpress.com/eXpressAppFramework/402141/getting-started/in-depth-tutorial-blazor/customize-data-display-and-view-layout/format-a-property-value)
- [Localize An Xaf Application](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application)
- [Localize An Xaf Application#Single Language Support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)
- [Devexpress.Expressapp.Scheduler.Blazor.Scheduleroptions.Viewtypes?P=Net8](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1311731: Custom EasyTest Commands | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 610

**Summary:** The customer provided feedback regarding the lack of Blazor instructions on the DevExpress documentation page for custom EasyTest commands. They indicated that the page was not helpful and suggested the addition of sample code and information. The ticket includes links to related documentation for f...

---

##### 📦 T1313595: Describe why  "unsafe-inline" in CSP is required in XAF Blazor Apps

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The customer is inquiring about the necessity of using the "unsafe-inline" attribute in the Content Security Policy (CSP) for XAF Blazor Apps. It has been clarified that it is not possible to avoid using this attribute. A solution outlining the reasons for this requirement has been suggested, indica...

**Issue:** The customer doesn't understand whether it is possible to avoid using this attribute (not possible)

**Proposed Solution:** Write a section similar to this one:
[Why unsafe-inline Style Source is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)

Contact <PERSON> R for any questions

---

##### 📦 T1313180: The translation dialog appears in browser, as the language is changed several seconds after app loading

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue described involves a translation dialog appearing in the browser when a user opens an XAF app due to a delay in the language setting from "en" to "cs". This occurs as the browser initially receives `<html lang="en" />` content, which is later dynamically changed. The solution involves cus...

**Issue:** When user opens XAF app, browser receives `<html lang="en" />` content which is dynamically changed to lang="cs" in few seconds. In between browser shows the translation popup.

**Proposed Solution:** Add information to the [Single language support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support) section:

To resolve the issue, customize the `<html>` tag in the `Pages\_Host.cshtml` file In XAF Blazor application.  Specify the correct culture: `<html lang="cs" />` . After that, the correct culture should be set since the i...

---

##### 📦 T1303299: Scehduler configuration docs are difficult to find

**Status:** Archived  
**Gap Type:** Discoverability Gap  
**Customer References:** 1  
**Priority Score:** 430

**Summary:** The customer expressed dissatisfaction with the difficulty in locating code snippets for Scheduler configuration. The primary issue is not the absence of snippets but their accessibility and discoverability via search engines. A specific code snippet is found in the help topic regarding SchedulerOpt...

**Issue:** The customer is unhappy with the lack of code snippets regarding Scheduler configuration. However, the real issue lies in the fact that those code snippets are difficult to find.

We have a code snippet in the following help topic: [SchedulerOptions\.ViewTypes Property](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8).

Howev...

---

##### ✅ T1309006: Format a Property Value | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 320

**Summary:** The customer encountered an issue with the documentation regarding the `DisplayFormat` property not being available in the 25.1 version of the product. They suggested improvements to the documentation, particularly related to formatting property values for the `DueDate` and `StartDate` nodes in thei...

---

##### 📦 T1300308: Missing info about contradiction between Template Localization and Satellite Assemblies (Localization Service)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer is experiencing confusion due to missing information in the help topics regarding the interaction between Template Localization and Satellite Assemblies in the localization process. Template Localization takes priority over Satellite Assemblies, which may lead to issues when attempting ...

**Issue:** There's a lack of information in our help topics regarding how two different ways of control localization interact with each other: 

1. Template Localization.
2. Satellite Assemblies (Localization Service).

Template Localization exports all localizable strings to the "Localization" node of the Application Model. This leads to XAF's localization mechanisms completely ignoring any data from Satell...

**Proposed Solution:** Add the described information to the related help topics.

---


### [Core] Fluent UI Icon and Layout Updates in XAF WinForms

**Issues:** 5 (4 unresolved)  
**Affected Documentation:** 11 URL(s)  
**Estimated Effort:** 8 hours

#### 📄 Affected Documentation Topics

- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [Format A Business Object Caption?V=22.1](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [Active Directory And Oauth2 Authentication Providers In Winforms Applications](https://docs.devexpress.com/eXpressAppFramework/404752/data-security-and-safety/security-system/authentication/oauth-and-custom-authentication/active-directory-and-oauth2-authentication-providers-in-winforms-applications)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Model.Imodelclass.Objectcaptionformat](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Model.IModelClass.ObjectCaptionFormat)
- [Devexpress.Persistent.Base.Objectcaptionformatattribute](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Persistent.Base.ObjectCaptionFormatAttribute)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1285906: OAuth and Custom Authentication - a crucial aspect is not emphasized

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue highlights a missing detail in the documentation regarding the `NameClaimType` value in OAuth and Custom Authentication for applications using `DevExpress.ExpressApp.Security.UserManager`. It is critical for the `ClaimsIdentity.Name` value to be present when parsing a principal from a thir...

**Issue:** Help topics of this help section miss the crucial piece of information - the necessity to set the `NameClaimType` value. The reason for this is that our `DevExpress.ExpressApp.Security.UserManager` class expects the [ClaimsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsidentity.name?view=net-9.0#remarks) value to exist (e.g., to be not null) when parsing a...

**Proposed Solution:** Reflect this information in our documentation and emphasize its importance.

---

##### 📦 T1315692: ObjectCaptionFormatAttribute Class - old info was lost

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer reported that the information from an old help topic, "Format a Business Object Caption," was not transferred to the current documentation of the "ObjectCaptionFormatAttribute Class." The solution proposed is to add the relevant information, including screenshots and examples, from the ...

**Issue:** We had the following help topic, which is now discontinued: [Format a Business Object Caption](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1). Selecting a newer version redirects to [ObjectCaptionFormatAttribute Class](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Pers...

**Proposed Solution:** Add the information from the old help topic to the attribute's help topic.

---


### [Core] WinForms Filter Editor - Dynamic Expressions

**Issues:** 4 (4 unresolved)  
**Affected Documentation:** 10 URL(s)  
**Estimated Effort:** 8 hours

#### 📄 Affected Documentation Topics

- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [Format A Business Object Caption?V=22.1](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [Active Directory And Oauth2 Authentication Providers In Winforms Applications](https://docs.devexpress.com/eXpressAppFramework/404752/data-security-and-safety/security-system/authentication/oauth-and-custom-authentication/active-directory-and-oauth2-authentication-providers-in-winforms-applications)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Model.Imodelclass.Objectcaptionformat](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Model.IModelClass.ObjectCaptionFormat)
- [Devexpress.Persistent.Base.Objectcaptionformatattribute](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Persistent.Base.ObjectCaptionFormatAttribute)

#### 🎫 Documentation Issues

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1285906: OAuth and Custom Authentication - a crucial aspect is not emphasized

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue highlights a missing detail in the documentation regarding the `NameClaimType` value in OAuth and Custom Authentication for applications using `DevExpress.ExpressApp.Security.UserManager`. It is critical for the `ClaimsIdentity.Name` value to be present when parsing a principal from a thir...

**Issue:** Help topics of this help section miss the crucial piece of information - the necessity to set the `NameClaimType` value. The reason for this is that our `DevExpress.ExpressApp.Security.UserManager` class expects the [ClaimsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsidentity.name?view=net-9.0#remarks) value to exist (e.g., to be not null) when parsing a...

**Proposed Solution:** Reflect this information in our documentation and emphasize its importance.

---

##### 📦 T1315692: ObjectCaptionFormatAttribute Class - old info was lost

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer reported that the information from an old help topic, "Format a Business Object Caption," was not transferred to the current documentation of the "ObjectCaptionFormatAttribute Class." The solution proposed is to add the relevant information, including screenshots and examples, from the ...

**Issue:** We had the following help topic, which is now discontinued: [Format a Business Object Caption](https://docs.devexpress.com/eXpressAppFramework/112752/getting-started/in-depth-tutorial-winforms-webforms/ui-customization/format-a-business-object-caption?v=22.1). Selecting a newer version redirects to [ObjectCaptionFormatAttribute Class](https://docs.devexpress.com/eXpressAppFramework/DevExpress.Pers...

**Proposed Solution:** Add the information from the old help topic to the attribute's help topic.

---


### [Blazor] Editors

**Issues:** 4 (3 unresolved)  
**Affected Documentation:** 2 URL(s)  
**Estimated Effort:** 6 hours

#### 📄 Affected Documentation Topics

- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)

#### 🎫 Documentation Issues

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1282060: Implement a Property Editor Based on a Custom Component 

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 310

**Summary:** The user is requesting assistance with implementing a property editor based on a custom component, as the referenced article does not provide guidance on using a custom component. The proposed solution is to include an example with a custom razor component.

**Issue:** the article 'Implement a Property Editor Based on a Custom Component' doesn't show how to use a custom component at all.

**Proposed Solution:** We need to add an example with a custom razor component

---

##### ✅ T1314388: You have a new 'GitHub Examples  User Feedback' response.

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 120

**Summary:** The customer provided feedback regarding the 'WinHyperLinkStringPropertyEditor' example, stating that it does not respond to clicks while used in a nested listView. After review, it was identified that the expected behavior involves selecting a cell and double-clicking the link to follow it, which m...

---


### [Blazor] Performance - Simplified Blazor Components

**Issues:** 12 (10 unresolved)  
**Affected Documentation:** 13 URL(s)  
**Estimated Effort:** 20 hours

#### 📄 Affected Documentation Topics

- [Content Security Policy#Why Unsafe Inline Style Source Is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)
- [How To Create A Custom Winforms Ribbon Template](https://docs.devexpress.com/eXpressAppFramework/112618/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-ribbon-template)
- [Add And Replace Icons](https://docs.devexpress.com/eXpressAppFramework/112792/app-shell-and-base-infrastructure/icons/add-and-replace-icons)
- [View Variants Module](https://docs.devexpress.com/eXpressAppFramework/113011/app-shell-and-base-infrastructure/view-variants-module)
- [How To Distribute Custom Templates With Modules](https://docs.devexpress.com/eXpressAppFramework/113047/ui-construction/templates/how-to-distribute-custom-templates-with-modules)
- [Custom Easy Test Commands](https://docs.devexpress.com/eXpressAppFramework/113340/debugging-testing-and-error-handling/functional-tests-easy-test/write-tests-human-readable/custom-easy-test-commands)
- [How To Create A Custom Winforms Standard Template](https://docs.devexpress.com/eXpressAppFramework/113706/ui-construction/templates/in-winforms/how-to-create-a-custom-winforms-standard-template)
- [Localize An Xaf Application#Single Language Support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support)
- [Winforms Application Templates](https://docs.devexpress.com/eXpressAppFramework/403446/ui-construction/templates/winforms-application-templates)
- [How To Show A Custom Data Bound Control In An Xaf Blazor Basic](https://docs.devexpress.com/eXpressAppFramework/404698/ui-construction/view-items-and-property-editors/how-to-show-a-custom-data-bound-control-in-an-xaf-view/how-to-show-a-custom-data-bound-control-in-an-xaf-blazor-basic)
- [Devexpress.Expressapp.Blazor.Blazorapplication.Icontype](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.BlazorApplication.IconType)
- [Devexpress.Expressapp.Blazor.Editors.Blazorcontrolviewitem#Remarks](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks)
- [Devexpress.Expressapp.Scheduler.Blazor.Scheduleroptions.Viewtypes?P=Net8](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8)

#### 🎫 Documentation Issues

##### ✅ T1303785: View Variants (Switch Document Layouts) | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 9  
**Priority Score:** 810

**Summary:** The customer provided feedback regarding the DevExpress documentation on handling view variants in the EF Main Demo application. Specifically, they noted that the article referenced does not work as expected when adding views and variants to the model.xafml file in the Blazor Server application. It ...

---

##### 📦 T1309586: Improve BlazorControlViewItem help topic

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 710

**Summary:** The customer has reported that the help topic for `BlazorControlViewItem` is unclear and suggested a more explicit explanation in the Remarks section. They recommend including specific instructions on creating a new razor component in the Editors folder of the Blazor project to enhance clarity for u...

**Issue:** The [BlazorControlViewItem](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem#remarks) help topic is unclear

It says the following:

> The following code snippet uses `BlazorControlViewItem` to create a custom component:  
> **File:** *CS\\MainDemo.Blazor.Server\\Editors\\ButtonComponent.razor*

Initially, I thought that it recommends to lo...

**Proposed Solution:** Write something like that in Remarks section:  
> Create a new razor component in the Editors folder of your Blazor project. Add the following markup there:

---

##### 📦 T1317092: Add and Replace Icons | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 700

**Summary:** The customer provided feedback regarding the DevExpress documentation about adding and replacing icons, stating that the information was mostly relevant for WinForms and appeared outdated. They suggested updating the content to make it more applicable for Blazor applications, where features like `Im...

---

##### 📦 T1309299: Readme of the 'sequential generator' example is outdated

**Status:** Archived  
**Gap Type:** True Gap  
**Customer References:** 1  
**Priority Score:** 650

**Summary:** The issue raised is regarding the outdated Readme of the 'sequential generator' example, specifically within the XPO documentation. The user points out that it does not reflect the latest changes related to the configuration for MiddleTier+Multitenancy and MiddleTier+Blazor setups. The suggested sol...

**Issue:** [https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/22.2.4%2B/CS/XPO/SequenceGenerator) Readmes (XPO in particular) doesn't reflect latest changes. E.g. ...

**Proposed Solution:** Contact developers to get the most precise code for these cases.

---

##### 📦 T1314402: Missing one step of the process - Implement a Property Editor Based on a Custom Component (Blazor)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 4  
**Priority Score:** 650

**Summary:** Multiple customers have experienced confusion while implementing a custom control based on existing instructions for a Razor component (`InputText`). The existing help topic fails to demonstrate the necessary steps for customers creating their own Razor pages. To address this issue, two potential so...

**Issue:** Multiple customers (not too many though) experienced an issue understanding the process of implementing a custom control while following the instructions from this help topic. The reason for that lies in the fact that the help topic's description based on an already existing Razor component (`InputText`) and relies on our inner mechanisms to tie Component Model to the Razor component's parameters....

**Proposed Solution:** 1 (simple):
Enhance the help topic to implement the `InputText` control through a custom Razor wrapper page for demonstration purposes.

---

##### 📦 T1286784: FROM PM: Add a note about Visual Studio code style settings, which lead to runtime errors

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 620

**Summary:** This ticket addresses an issue reported by two customers regarding runtime errors in their applications due to Visual Studio code style settings that affect the WinForms designer. The main problem is that the `this` access qualifier may be removed when forms are modified and saved in the designer, l...

**Issue:** 1. It was reported by two customers, the last time in [Form Designer Breaks form on any change]({'FriendlyId':'T1286701','HashCode':'','CheckAnswerDesk':'7bb212e9-1af8-4a62-a4b6-fd592cbadb44'}). 
2. Unfortunately, it is very difficult to diagnose and I myself had to consult with the WinForms team: [<PERSON>: ? InitializeComponent (XXX.designer.cs) ???????? WinForms ??????? ...](https://teams.micro...

**Proposed Solution:** Add a red note 

>Microsoft WinForms designer code generation is fully controlled by your Visual Studio and project settings. If you modify and save your forms in the designer, the `this` access qualifier may be removed and runtime errors will occur as a result. For example, your DetailRibbonForm1.designer.cs file will define all components as "ribbonControl.XXX" instead of "this.ribbonControl.XXX...

---

##### 📦 T1311731: Custom EasyTest Commands | XAF: Cross-Platform .NET App UI & Web API | DevExpress Documentation

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 10  
**Priority Score:** 610

**Summary:** The customer provided feedback regarding the lack of Blazor instructions on the DevExpress documentation page for custom EasyTest commands. They indicated that the page was not helpful and suggested the addition of sample code and information. The ticket includes links to related documentation for f...

---

##### 📦 T1313595: Describe why  "unsafe-inline" in CSP is required in XAF Blazor Apps

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The customer is inquiring about the necessity of using the "unsafe-inline" attribute in the Content Security Policy (CSP) for XAF Blazor Apps. It has been clarified that it is not possible to avoid using this attribute. A solution outlining the reasons for this requirement has been suggested, indica...

**Issue:** The customer doesn't understand whether it is possible to avoid using this attribute (not possible)

**Proposed Solution:** Write a section similar to this one:
[Why unsafe-inline Style Source is Required](https://docs.devexpress.com/Blazor/403487/security-considerations/content-security-policy#why-unsafe-inline-style-source-is-required)

Contact <PERSON> R for any questions

---

##### 📦 T1313180: The translation dialog appears in browser, as the language is changed several seconds after app loading

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue described involves a translation dialog appearing in the browser when a user opens an XAF app due to a delay in the language setting from "en" to "cs". This occurs as the browser initially receives `<html lang="en" />` content, which is later dynamically changed. The solution involves cus...

**Issue:** When user opens XAF app, browser receives `<html lang="en" />` content which is dynamically changed to lang="cs" in few seconds. In between browser shows the translation popup.

**Proposed Solution:** Add information to the [Single language support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support) section:

To resolve the issue, customize the `<html>` tag in the `Pages\_Host.cshtml` file In XAF Blazor application.  Specify the correct culture: `<html lang="cs" />` . After that, the correct culture should be set since the i...

---

##### 📦 T1303299: Scehduler configuration docs are difficult to find

**Status:** Archived  
**Gap Type:** Discoverability Gap  
**Customer References:** 1  
**Priority Score:** 430

**Summary:** The customer expressed dissatisfaction with the difficulty in locating code snippets for Scheduler configuration. The primary issue is not the absence of snippets but their accessibility and discoverability via search engines. A specific code snippet is found in the help topic regarding SchedulerOpt...

**Issue:** The customer is unhappy with the lack of code snippets regarding Scheduler configuration. However, the real issue lies in the fact that those code snippets are difficult to find.

We have a code snippet in the following help topic: [SchedulerOptions\.ViewTypes Property](https://docs.devexpress.com/eXpressAppFramework/DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions.ViewTypes?p=net8).

Howev...

---

##### 📦 T1282060: Implement a Property Editor Based on a Custom Component 

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 310

**Summary:** The user is requesting assistance with implementing a property editor based on a custom component, as the referenced article does not provide guidance on using a custom component. The proposed solution is to include an example with a custom razor component.

**Issue:** the article 'Implement a Property Editor Based on a Custom Component' doesn't show how to use a custom component at all.

**Proposed Solution:** We need to add an example with a custom razor component

---

##### ✅ T1314393: You have a new 'GitHub Examples  User Feedback' response.

**Status:** Closed  
**Gap Type:** Quality Gap  
**Customer References:** 0  
**Priority Score:** 130

**Summary:** The customer provided feedback on a GitHub example related to importing data in DevExpress UI components. They have been using these components for over 6 years but found the example unhelpful as it did not demonstrate how to import real data by browsing for a file. Suggestions for improvement were ...

---


### [Blazor] Aspire development and deployment project template

**Issues:** 1 (1 unresolved)  
**Affected Documentation:** 3 URL(s)  
**Estimated Effort:** 2 hours

#### 📄 Affected Documentation Topics

- [Localize An Xaf Application Net Framework](https://docs.devexpress.com/eXpressAppFramework/113250/localization/localize-an-xaf-application-net-framework)
- [How To Localize A Winforms Template](https://docs.devexpress.com/eXpressAppFramework/114495/localization/how-to-localize-a-winforms-template)
- [Localize An Xaf Application](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application)

#### 🎫 Documentation Issues

##### 📦 T1300308: Missing info about contradiction between Template Localization and Satellite Assemblies (Localization Service)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer is experiencing confusion due to missing information in the help topics regarding the interaction between Template Localization and Satellite Assemblies in the localization process. Template Localization takes priority over Satellite Assemblies, which may lead to issues when attempting ...

**Issue:** There's a lack of information in our help topics regarding how two different ways of control localization interact with each other: 

1. Template Localization.
2. Satellite Assemblies (Localization Service).

Template Localization exports all localizable strings to the "Localization" node of the Application Model. This leads to XAF's localization mechanisms completely ignoring any data from Satell...

**Proposed Solution:** Add the described information to the related help topics.

---



## P3 LOW POST RELEASE

**🟢 LOW PRIORITY - POST-RELEASE**
Minor improvements that can be addressed in future updates.

---

### [Core] XAF Integration with DevExpress Localization Tool

**Issues:** 2 (2 unresolved)  
**Affected Documentation:** 4 URL(s)  
**Estimated Effort:** 4 hours

#### 📄 Affected Documentation Topics

- [Localize An Xaf Application Net Framework](https://docs.devexpress.com/eXpressAppFramework/113250/localization/localize-an-xaf-application-net-framework)
- [How To Localize A Winforms Template](https://docs.devexpress.com/eXpressAppFramework/114495/localization/how-to-localize-a-winforms-template)
- [Localize An Xaf Application](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application)
- [Localize An Xaf Application#Single Language Support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support)

#### 🎫 Documentation Issues

##### 📦 T1313180: The translation dialog appears in browser, as the language is changed several seconds after app loading

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 520

**Summary:** The issue described involves a translation dialog appearing in the browser when a user opens an XAF app due to a delay in the language setting from "en" to "cs". This occurs as the browser initially receives `<html lang="en" />` content, which is later dynamically changed. The solution involves cus...

**Issue:** When user opens XAF app, browser receives `<html lang="en" />` content which is dynamically changed to lang="cs" in few seconds. In between browser shows the translation popup.

**Proposed Solution:** Add information to the [Single language support](https://docs.devexpress.com/eXpressAppFramework/402956/localization/localize-an-xaf-application#single-language-support) section:

To resolve the issue, customize the `<html>` tag in the `Pages\_Host.cshtml` file In XAF Blazor application.  Specify the correct culture: `<html lang="cs" />` . After that, the correct culture should be set since the i...

---

##### 📦 T1300308: Missing info about contradiction between Template Localization and Satellite Assemblies (Localization Service)

**Status:** Archived  
**Gap Type:** Quality Gap  
**Customer References:** 1  
**Priority Score:** 320

**Summary:** The customer is experiencing confusion due to missing information in the help topics regarding the interaction between Template Localization and Satellite Assemblies in the localization process. Template Localization takes priority over Satellite Assemblies, which may lead to issues when attempting ...

**Issue:** There's a lack of information in our help topics regarding how two different ways of control localization interact with each other: 

1. Template Localization.
2. Satellite Assemblies (Localization Service).

Template Localization exports all localizable strings to the "Localization" node of the Application Model. This leads to XAF's localization mechanisms completely ignoring any data from Satell...

**Proposed Solution:** Add the described information to the related help topics.

---


## 📝 Features Requiring Proactive Documentation

These 26.1 features have **no reported documentation issues**. 
Write documentation **before release** to avoid post-launch support tickets.

- **[Core]** DateTimeOffset support
- **[Blazor]** Electron.NET Example
- **[Blazor]** ContextMenu integration
- **[Blazor]** PivotTable
- **[Blazor]** FieldPickerPropertyEditor
- **[Blazor]** Additional Performance Researches

**Recommendation:** Allocate 8-12 hours for proactive documentation of new features.

---

## Appendix: Non-Roadmap Issues

**Count:** 1 issues not directly aligned with 26.1 roadmap

These issues should still be addressed but are not tied to specific 26.1 features:

- 📦 **T1303625**: Display a Tree List using the ITreeNode Interface | XAF: Cross-Platform .NET App

---

## Next Steps

1. **Assign P0 Critical issues** to documentation team immediately
2. **Review P1 High Priority** issues and schedule before release
3. **Create proactive documentation** for new features without issues
4. **Schedule P2 Medium Priority** issues for post-release sprint
5. **Monitor customer feedback** after 26.1 release for new documentation needs

---

*Report generated by XAF Documentation Analysis Pipeline*  
*Source: Phase 0 Analysis - 26 UNFIXED documentation issues requiring action*  
*Excluded: 31 tickets already marked as DocIssueFixed*
