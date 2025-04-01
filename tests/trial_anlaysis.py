import logging
from typing import Tuple, Optional
import pandas as pd
import matplotlib.pyplot as plt
from trial_eligibility import load_patient_data, load_trial_criteria, assign_trial_groups

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def analyze_eligibility() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Process patient data and return eligible/ineligible patients."""
    try:
        logger.info("Loading patient data...")
        patients = load_patient_data()
        
        if patients.empty:
            logger.error("No patient data loaded")
            raise ValueError("Patient data is empty")
            
        criteria = load_trial_criteria()
        
        logger.info(f"Processing {len(patients)} patients for trial eligibility")
        results = assign_trial_groups(patients, criteria)
        
        if results.empty:
            logger.error("No results after processing")
            raise ValueError("No results after trial group assignment")
        
        # Filter based on trial_group instead
        eligible = results[results['trial_group'].isin(['Group A', 'Group B'])]
        ineligible = results[results['trial_group'] == 'Not eligible']
        
        logger.info(f"Found {len(eligible)} eligible and {len(ineligible)} ineligible patients")
        return eligible, ineligible
    except Exception as e:
        logger.error(f"Error in eligibility analysis: {str(e)}")
        raise

def plot_ineligibility_reasons(ineligible: pd.DataFrame, 
                             output_path: str = "ineligibility_reasons.png") -> None:
    """Create and save visualization of ineligibility reasons."""
    try:
        if ineligible.empty:
            logger.warning("No ineligible patients to plot")
            return
            
        # Count ineligible reasons based on trial_group
        reason_counts = ineligible['trial_group'].value_counts()
        
        if len(reason_counts) == 0:
            logger.warning("No trial group data to plot")
            return

        # Create plot
        plt.figure(figsize=(10, 6))
        reason_counts.plot(kind='barh', color='salmon', edgecolor='black')
        plt.title(f"Trial Ineligibility Distribution (n={len(ineligible)})")
        plt.xlabel("Number of Patients")
        plt.ylabel("Group")
        plt.tight_layout()
        plt.grid(axis='x', linestyle='--', alpha=0.5)

        # Save and display
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.show()
        logger.info(f"Plot saved to {output_path}")
    except Exception as e:
        logger.error(f"Error creating plot: {str(e)}")
        raise

def main():
    """Main execution function."""
    try:
        # Run analysis
        eligible, ineligible = analyze_eligibility()
        
        # Display results
        print("\nEligible Patients:")
        if not eligible.empty:
            print(eligible[['Patient_ID', 'Age', 'Diagnosis_Code', 'trial_group']])
        else:
            print("No eligible patients found")
        
        print("\nIneligible Patients:")
        if not ineligible.empty:
            print(ineligible[['Patient_ID', 'Age', 'Diagnosis_Code', 'trial_group']])
        else:
            print("No ineligible patients found")
        
        # Create visualization only if we have data
        if not ineligible.empty:
            plot_ineligibility_reasons(ineligible)
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
