import fs from 'fs';
import { parse } from 'csv-parse';
import fg from 'fast-glob';

const files = await fg('**/*.csv');

for (const file of files) {
  console.log(`Parsing: ${file}`);
  fs.createReadStream(file)
    .pipe(
      parse({
        columns: true,
        skip_empty_lines: true,
        trim: true,
      }),
    )
    // .on('data', (record) => console.log(record))
    .on('end', () => console.log(`Finished ${file}`))
    .on('error', (err) => console.error(`Error in ${file}:`, err.message));
}
