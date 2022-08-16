[Back](./README.md)

# WHS Android

## Technical Documentation

### GETTING STARTED

### INSTALLATION AND DEVELOPMENT

In order to start the development, first, you need to start Android Studio. Import the Agtech-2021WHS project and then wait for the build to finish.

### PROGRAMMING LANGUAGE

WHS uses Kotlin for development

### MINIMUM VERSION

WHS can run on Android Systems with minimum SDK version 16 (Jellybean). It may encounter multiple issues on lower SDK versions.

### APPLICATION ID
com.au.whs.agtech

### DEBUGGING

We use Android Virtual Device in Android Studio in order to test the Native Apps in different screen sizes and SDK Versions.

### THIRD-PARTY LIBRARIES

Most of the third-party libraries are integrated using Gradle. They can be added by searching library names found in the Dependencies tab in the Project Structure window.

#### Important Libraries

- **Firebase/Crashlytics** - used to report crashes from Users that are not encountered during development and debugging.
- **RxJava** - is a concurrency design pattern that you can use on Android to simplify code that executes asynchronously.
- **Retrofit** - is type-safe REST client for Android and Java which aims to make it easier to consume RESTful web services.

#### Main Utilities
- **NetworkUtils** - a class where network related functions are placed
- **ActionApi** - a class that contains action endpoints
- **ApiConnection** - a class where API connection is configured
- **AttachmentApi** - a class that contains attachment endpoints

#### Activities/Fragments

- **MainActivity** - is the main activity that contains the child fragments and sibling activities
- **LoginActivity** - handles the login screen
- **SearchActivity** - handles the search page
- **SettingsActivity** - handles the settings page
- **PdfViewerActivity** - handles the PDF viewer page
- **HazardActivity** - handles the hazard page
- **EmailReportActivity** - handles the email report page
- **ActionListActivity** - handles the action list page
- **AddEditActionActivity** - handles the add, edit action page
- **AttachmentDetailActivity** - handles the attachment details page
- **AttachmentListActivity** - handles the attachment list page
- **ChangePasswordActivity** - handles the change password page
- **ChemicalRegisterActivity** - handles the chemical registry page
- **MsdsProductDetailActivity** - handles the product detail page
- **MsdsSearchResultActivity** - handles the search result page
- **RecordDetailActivity** - handles the record detail page
- **RecordSearchResultActivity** - handles the record search result page
- **RecordTabsActivity** - handles the record tabs page
- **ReferenceFormActivity** - contains the reference form
- **ReferenceListActivity** - handles the reference list page
- **TimeSheetActivity** - handles the time sheet page
- **BeaconTimeInActivity** - handles the beacon time in page
- **NFCTimeInActivity** - handles the NFC time in page
- **QrTimeInActivity** - handles the QR time in page
- **TaskFormActivity** - handles the task form page
- **MobileVerificationActivity** - handles the mobile verification page
- **SigneeFormActivity** - handles the signee form page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- //FRAGMENT-ACTION
- **RegisterActionFragment** - handles the register page
- **RiskAssessmentActionFragment** - handles the risk assessment page
- **SwmsActionFragment** - handles the swms page    
- //FRAGMENT-ATTACHMENT
- **AttachmentDetailFragment** - handles the attachment details page
- **AttachmentlistFragment** - handles the attachment lists page    
- //FRAGMENT-AUDIT   
- **CheckListHazardFragment** - handles the checklist hazard page    
-  //FRAGMENT-CHEMICALS-ESQ 
- **EsqBatchFormFragment** - handles the esq batch form page
-  **EsqMainFormFragment** - handles the esq main form page
-  //FRAGMENT-CHEMICALS
-  **ChemicalManifestListFragment** - handles the checmical manifest list page
-  **ChemicalManifestSummaryFragment** - handles the chemical manifest summary page
-  **ChemicalRegisterDetailFragment** - handles the chemical register detail page
-  **ChemicalRegisterFragment** - handles the chemical register page
-  **MsdsProductDetailFragment** - handles the msds product detail page
-  **MsdsSearchFragment** - handles the msds search page
-  **MsdsSearchResultFragment** - handles the msds search result page
-  //FRAGMENT-DYNAMICTEMPLATE
-  **AddDataTemplateFragment** - handles the add data template page
-  **DynamicDetailFormFragment** - handles the dynamic detail form page
-  **DynamicTemplateFormFragment** - handles the dynamic template form page
-  **DynamicTemplateListFragment** - handles the dynamic template list page
-  **TemplateFormFragment** - handles the template form page
-  //FRAGMENT-HAZARD
-  **HazardFormFragment** - handles the hazard form page
-  **HazardFormPresenter** - handles the hazard presenter page
-  **HazardFormView** - handles the hazard form view page
-  **HazardTemplateFragment** - handles the hazard template page
-  **HazardTemplatePresenter** - handles the hazard template presenter page
-  **HazardTemplateView** - handles the hazard template view page
-  //FRAGMENT-INCIDENT
-  **IncidentAdditionalFragment** - handles the incident addtional page
-  **IncidentAssessmentFragment** - handles the incident assessment page
-  **IncidentDetailFragment** - handles the incident detail page
-  **IncidentHazardDetailsFragment** - handles the incident hazard details page
-  **IncidentHazardFormFragment** - handles the incident hazard form page
-  **IncidentSimplifiedDetailFragment** - handles the incident simplified detail page
-  **InicdentTreatmentFragment** - handles the incident treatment page
-  **IncidentWitnessFormFragment** - handles the incident witness form page
-   //FRAGMENT-INSPECTION
-   **InspectionDetailFormFragment** - handles the inspection detail form page
-   //FRAGMENT-LOCAL
-   **LocalAuditFragment** - handles the local audit page
-   **LocalDynamicFragment** - handles the local dynamic page
-   **LocalFormsFragment** - handles the local forms page
-   **LocalHazardFragment** - handles the local hazard page
-   **LocalReportIncidentFragment** - handles the local report incident page
-   **LocalSubSecletionActivity** -  handles the local sub-selection activity page
-   //FRAGMENT-REFERENCE
-   **ExposureLimitReferenceFragment** - handles the exposure limit reference page
-   **GeneralReferenceFragment** - handles the general reference page
-   **LocationReferenceFragment** - handles the location reference page
-   **MapFragment** - handles the map page
-   **ReferenceExposureListFragment** - handles the reference exposure list page                                
-   **ReferenceListFragment** - handles the reference list page
-   **RiskControlReferenceFragment** - handles the risk control reference page
-   **SubTypeReferenceFragment** - handles the sub type reference page 
-   **TypeReferenceFragment** - handles the type reference page
-   **WorkerReferenceFragment** - handles the worker reference page
-   //FRAGMENT-REGISTER-ENVIRONMENTAL
-   **AtmosphericDetailsFragment** - handles the atmospheric details page
-   **ConfinedSpacesDetailsFragment** - handles the confined spaces details page
-   **CustomSubscriber** - handles the custom subscriber page
-   **EntryDetailsFragment** - handles the entry details page
-   **MeasurementDetailsFragment** - handles the measurement details page
-   **MonitoringHistoryFragment ** - handles the monitoring history page
-   **NoiseAssessmentDetailFragment** - handles the noice assessnent detail page
-   **NoiseControlAssessmentFragment** - handles the noise control assessment page
-   **NoiseControlDetailsFragment** - handles the noise control details page
-   **PermitFragment** - handles the permit page
-   //FRAGMENT-REGISTER-HAZARD
-   **EmployeeExposureFragment** - handles the employee exposure page
-   **RegisterAsbestosInspectionFragment** - handles the register asbestos inspection page
-   **RegisterAsbestosRemovalFragment** - handles the register asbestos removal page
-   **RegisterAsbestosFragment** - handles the register asbestos page
-   **RegisterCarcinogensFragment** - handles the register carcinogens page
-   //FRAGMENT-REGISTER-POLICY
-   **AttendeeDetailFragment** - handles the attendee detail page
-   **DrillDetailFormFragment** - handles the drill detail form page
-   **EmergencyProcedureFragment** - handles the emergency procedure page
-   **LegislationDetailFormFragment** - handles the legistlation detail form page
-   **MeetingsDetailFormFragment** - handles the meetings detail form page
-   **PointRaisedFormFragment** - handles the point raised form page
-   **RegisterPolicyDetailFormFragment** - handles the register policy detail form page
-   **TrainingDetailFormFragment** - handles the training detail form page
-   //FRAGMENT-REGISTER-SAFETY
-   **PpeEmployeeFragment** - handles the ppe employee page
-   **RegisterEmergencyFragment** - handles the register emergency page
-   **RegisterFireDetectFragment** - handles the register fire detect page
-   **RegisterFireFightingFragment** - handles the register fire fighting page
-   **RegisterFireAidFragment** - handles the register fire aid page
-   **RegisterSafetyServicingFragment** - handles the register safety servicing page
-   **RegisterSafetyTestingFragment** - handles the register safety testing page
-   **RegisterSpillKitFragment** - handles the register spill kit page
-   //FRAGMENT-REGISTER
-   **RegisterAssetDetailFragment** - handles the register asset detail page
-   **RegisterAssetServicingFragment** - handles the register asset servicing page
-   **RegisterAssetTestingFragment** - handles the register asset testing page
-   **RegisterHistoryFragment** - handles the register history page
-   //FRAGMENT-SEARCH
-   **ActionMonitorSearchFragment** - handles the action monitor search page
-   **AssetSearchFragment** - handles the asset search page
-   **AttendeeSearchFragment** - handles the attendee search page
-   **AuditSearchFragment** - handles the audit search page
-   **ConfinedSpaceSearchFragment** - handles the confined spage search page
-   **EnviornmentalSearchFragment** - handles the environmental search page
-   **HATSSearchFragment** - handles the HATS search fragment
-   **HazardSearchFragment** - handles the hazard search page
-   **IncidentSearchFragment** - handles the incident search page
-   **PolicySearchFragment** - handles the policy search page
-   **QChartSearchFragment** - handles the Q chart search page
-   **RiskAssessmentSearchFragment** - handles the risk assessment search page
-   **SiteRiskSearchFragment** - handles the site risk search page
-   **SwmsSearchFragment** - handles the swms search page
-   **SwpSearchFragment** - handles the swp search page
-   //FRAGMENT-SITERISK 
-   **ControlFragment** - handles the control page
-   **NewSiteRiskFragment** - handles the new site risk page
-   **RiskDetailFragment** - handles the risk detail page
-   **RiskRatingFragment** - handles the risk rating page
-   **RiskFragment** - handles the risk page
-   **SiteRiskHazardFragment** - handles the site risk hazard page
-                 
-     


### TECHNICAL ARCHITECTURE

https://docs.google.com/presentation/d/1zwyqjWj-pD5GhJBKlKkLHscQwNlRJe6SFR_hmEWbIPk/edit?usp=sharing

#### **Model**

The model houses the logic for the program, which is retrieved by the ViewModel upon its own receipt of input from the user through View.
 
#### **View**

View is the collection of visible elements, which also receives user input. This includes user interfaces (UI), animations and text. The content of View is not interacted with directly to change what is presented.
#### **ViewModel**
ViewModel is located between the View and Model layers. This is where the controls for interacting with View are housed, while binding is used to connect the UI elements in View to the controls in ViewModel.





