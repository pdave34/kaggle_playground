# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from icecream import ic
import glob, os
import pandas as pd

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
        
        Assumes .csv files 
    """
    #ic.disable()

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    input_files = glob.glob(os.path.join(input_filepath, '*.csv'))
    logger.info(ic(f'found {len(input_files)} files: {input_files}'))

    for i, fi in enumerate(input_files):
        df = pd.read_csv(fi)
        logger.info(f'----------------------------------------')
        logger.info(f'        {fi}                            ')
        logger.info(f'----------------------------------------')
        ic(df.describe())
        ic(df.info())


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
